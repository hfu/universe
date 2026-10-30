#!/usr/bin/env python3
"""CATALOG.md を生成する(標準ライブラリのみ)。--check で最新性を検査。"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_universe import field, sections, split_front_matter  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def esc(s):
    return s.replace("|", "\\|").replace("\n", " ")


def build():
    rows = []
    for p in sorted((ROOT / "kcaim").glob("*.md")):
        raw = p.read_bytes()
        text = raw.decode("utf-8")
        fm, body, err = split_front_matter(text)
        if err:
            raise SystemExit(f"{p.name}: {err}")
        counts = {"pass": 0, "partial": 0, "fail": 0, "volatile": 0}
        for path, lines in sections(body):
            if path.startswith("/acceptance-tests/"):
                r = (field(lines, "result") or "").strip()
                if r in counts:
                    counts[r] += 1
        tests = "/".join(f"{k} {v}" for k, v in counts.items())
        size = f"{len(raw):,} B / {len(text):,} 字"
        rows.append(f"| [{esc(fm['id'])}](kcaim/{p.name}) | {esc(fm['title'])} | {fm['maintenance_tier']} "
                    f"| {fm['as_of']} | {esc(fm['scope'])} | {fm['license']} | {tests} | {size} |")
    ext = (ROOT / "EXTERNAL.md").read_text(encoding="utf-8")
    tbl = [ln for ln in ext.split("\n") if ln.startswith("|")]
    out = [
        "# CATALOG",
        "",
        "> このファイルは生成物である。`scripts/build_catalog.py` が作る。手で編集しない。",
        "",
        "## この universe の kcaim",
        "",
        "| id | title | tier | as_of | scope | license | tests | size |",
        "|---|---|---|---|---|---|---|---|",
        *rows,
        "",
        "## 外部の kcaim",
        "",
        "(EXTERNAL.md の表をそのまま埋め込んでいる)",
        "",
        *tbl,
        "",
    ]
    return "\n".join(out)


def main():
    new = build()
    path = ROOT / "CATALOG.md"
    if "--check" in sys.argv:
        if not path.exists() or path.read_text(encoding="utf-8") != new:
            print("CATALOG.md が最新でない。`python3 scripts/build_catalog.py` を実行する。")
            return 1
        print("CATALOG.md は最新")
        return 0
    path.write_text(new, encoding="utf-8")
    print("CATALOG.md を生成した")
    return 0


if __name__ == "__main__":
    sys.exit(main())
