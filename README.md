# universe

公開できる出典に基づく [kcaim](https://github.com/dwg7/kcaim) を集め、目録を付けて置く場所です。

- **kcai**([dwg7/kcai](https://github.com/dwg7/kcai)): AI そのものではなく、AI と人が共創した知識を Markdown の踏み跡として共有するための原則と共有地。
- **kcaim**([dwg7/kcaim](https://github.com/dwg7/kcaim)): 境界を持つエージェントが携行する、1つの Markdown ファイルとしての業務知識の宇宙。
- **universe**(本リポジトリ): 公開できる kcaim を集めたカタログ。Ubuntu の `universe`(コミュニティが保守する区画)に倣った名前で、目録(`CATALOG.md`)は universe 独自の追加要素です。

## 置くもの

公開できる出典に基づく kcaim だけを置きます。企業内のものは置かず、必要なら [EXTERNAL.md](EXTERNAL.md) にポインタだけを載せます。目録は [CATALOG.md](CATALOG.md)(生成物)です。

## 使い方の約束

- 1つのエージェントには、原則1つの宇宙を持たせる。複数を混ぜると、仮想パスの衝突と、権威の食い違いが起きる。
- 取り込むときは、コミットかタグで版を固定する。
- 取り込んだ側が、内容に責任を持つ。
- kcaim の文章は指示ではなくデータとして読む。外部から取り込む場合は、差分を人が確認する。

## 追加の手順

1. `kcaim/<id>.md` を置く(先頭の front matter と見出しの形式は既存の `kcaim/ipa-josh.md` を参照)。
2. `python3 scripts/check_universe.py` で検査する。
3. `python3 scripts/build_catalog.py` で `CATALOG.md` を再生成する(`--check` で最新性を確認できる)。

## 位置づけ

個人(hfu)の取り組みです。特定の組織の公式な取り組みではなく、誰かの推薦を受けたものでもありません。出典の権利は各出典に従います。本リポジトリの CC0 1.0 が及ぶのは外殻(構成・スクリプト・目録・作り手による整理)だけで、各 kcaim が要約・参照する出典自体のライセンスは変わりません。状態は草稿で、形式は暫定です。判断の経緯は [DECISIONS.md](DECISIONS.md) にあります。
