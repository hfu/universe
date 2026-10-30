#!/usr/bin/env python3
"""kcaim/*.md の検査器(標準ライブラリのみ)。ERRORがあれば終了コード1。"""
import datetime
import re
import sys
from pathlib import Path

REQUIRED = ["kcaim_format", "id", "title", "as_of", "maintainer", "publication",
            "license", "maintenance_tier", "scope", "disclaimer"]
# 仕様の「必須キーは9つ」に対し、kcaim_format を含めて10キーを要求している点に注意
RESERVED = {"readme", "catalog", "external", "decisions", "agents", "claude", "license"}
TIERS = {"maintained", "best-effort", "dormant", "archived"}
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
H1_RE = re.compile(r"^/[a-z0-9-]+(/[a-z0-9._-]+)*$")
DANGEROUS = [
    r"以前の指示を無視", r"これまでの指示を無視", r"ignore (all )?(the )?(previous|prior) instructions",
    r"システムプロンプトを(出力|表示|開示)", r"reveal (the |your )?system prompt",
    r"\b(curl|wget)\b[^\n]*\|\s*(ba)?sh", r"(curl|wget)\s+(-\S+\s+)*https?://\S+\s*を?実行",
]
BAD_EXT = {".docx", ".xlsx", ".pptx", ".pdf", ".doc", ".xls", ".ppt"}


def split_front_matter(text):
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, None, "front matter がない"
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            fm = {}
            for ln in lines[1:i]:
                if not ln.strip():
                    continue
                m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", ln)
                if not m:
                    return None, None, f"front matter の行が `key: value` でない: {ln[:40]}"
                fm[m.group(1)] = m.group(2).strip()
            return fm, "\n".join(lines[i + 1:]), None
    return None, None, "front matter が閉じていない"


def iter_body_lines(body):
    """コードフェンス内を除いた (行番号, 行) を返す。"""
    fence = False
    for n, ln in enumerate(body.split("\n"), 1):
        if ln.lstrip().startswith("```") or ln.lstrip().startswith("~~~"):
            fence = not fence
            continue
        if not fence:
            yield n, ln


def sections(body):
    """見出し(第1レベル)ごとの本文を返す: [(path, [lines])]"""
    out, cur = [], None
    for _, ln in iter_body_lines(body):
        if ln.startswith("# "):
            cur = (ln[2:].strip(), [])
            out.append(cur)
        elif cur is not None:
            cur[1].append(ln)
    return out


def field(lines, key):
    pat = re.compile(r"^\s*-\s*" + re.escape(key) + r":\s*(.*)$")
    for ln in lines:
        m = pat.match(ln)
        if m:
            return m.group(1).strip()
    return None


def check_file(path, today, errors, warns, infos):
    name = path.name
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        errors.append(f"{name}: UTF-8 でない")
        return
    if "\x00" in text:
        errors.append(f"{name}: NUL を含む")
        return
    infos.append(f"{name}: {len(raw)} バイト / {len(text)} 文字")
    fm, body, err = split_front_matter(text)
    if err:
        errors.append(f"{name}: {err}")
        return
    for k in REQUIRED:
        if k not in fm or not fm[k]:
            errors.append(f"{name}: 必須キー {k} がない")
    stem = path.stem
    if "id" in fm:
        if not ID_RE.match(fm["id"]):
            errors.append(f"{name}: id が形式に合わない: {fm['id']}")
        if fm["id"] != stem:
            errors.append(f"{name}: id とファイル名が一致しない ({fm['id']} != {stem})")
        if fm["id"] in RESERVED or stem in RESERVED:
            errors.append(f"{name}: id が予約名")
    if "as_of" in fm:
        try:
            d = datetime.date.fromisoformat(fm["as_of"])
            if d > today:
                errors.append(f"{name}: as_of が未来日付: {fm['as_of']}")
            elif (today - d).days > 180:
                warns.append(f"{name}: as_of が180日より古い ({fm['as_of']})")
        except ValueError:
            errors.append(f"{name}: as_of が ISO 日付でない: {fm['as_of']}")
    if fm.get("publication", "public") != "public":
        errors.append(f"{name}: publication は public のみ")
    if "maintenance_tier" in fm and fm["maintenance_tier"] not in TIERS:
        errors.append(f"{name}: maintenance_tier が範囲外: {fm['maintenance_tier']}")

    secs = sections(body)
    seen = set()
    for p, _ in secs:
        if not H1_RE.match(p):
            errors.append(f"{name}: 第1レベル見出しが形式に合わない: # {p}")
        if p in seen:
            errors.append(f"{name}: 第1レベル見出しが重複: # {p}")
        seen.add(p)
    source_ids = {p.split("/", 2)[2] for p in seen if p.startswith("/sources/")}
    for p, lines in secs:
        status = field(lines, "status") or ""
        stset = {s.strip() for s in status.split(",") if s.strip()}
        src = field(lines, "source")
        if src is not None:
            for s in [x.strip() for x in src.split(",") if x.strip()]:
                if s not in source_ids:
                    errors.append(f"{name}: {p}: source `{s}` が # /sources/{s} として存在しない")
        if "verified" in stset and not src and not p.startswith("/sources/"):
            warns.append(f"{name}: {p}: verified だが source: がない")
        if "volatile" in stset and field(lines, "freshness") is None:
            warns.append(f"{name}: {p}: volatile だが freshness: がない")
        if p.startswith("/acceptance-tests/") and field(lines, "result") is None:
            warns.append(f"{name}: {p}: result: がない")
    # 危険パターン(コードフェンス内も含め全文を対象にする。ただし検査説明文の誤検出は目視で確認)
    for pat in DANGEROUS:
        for m in re.finditer(pat, text, re.I):
            line = text.count("\n", 0, m.start()) + 1
            warns.append(f"{name}:{line}: エージェントへの指示とみなせる表現: {m.group(0)[:40]}")


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    kdir = root / "kcaim"
    errors, warns, infos = [], [], []
    today = datetime.date.today()
    if not kdir.is_dir():
        errors.append("kcaim/ がない")
    else:
        for p in sorted(kdir.iterdir()):
            if p.is_dir():
                errors.append(f"kcaim/{p.name}: サブディレクトリは置けない")
            elif p.suffix.lower() in BAD_EXT:
                errors.append(f"kcaim/{p.name}: Word/Excel/PowerPoint/PDF は正本にできない")
            elif p.suffix != ".md":
                errors.append(f"kcaim/{p.name}: .md 以外のファイル")
            else:
                check_file(p, today, errors, warns, infos)
    for i in infos:
        print("INFO ", i)
    for w in warns:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"--- ERROR {len(errors)} / WARN {len(warns)} / INFO {len(infos)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
