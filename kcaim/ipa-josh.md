---
kcaim_format: 0-draft
id: ipa-josh
title: IPA Japan Open Source Hub の公開資料に基づく OSS 導入・参加・OSPO 立ち上げの kcaim
as_of: 2026-10-30
maintainer: hfu
publication: public
license: CC0-1.0
maintenance_tier: maintained
scope: IPA の Japan Open Source Hub と、そこに掲載された公開資料に基づいて、OSS の導入・参加・組織づくり(特に OSPO の立ち上げ)に関する問いに答える。
disclaimer: 個人(hfu)による公開資料の整理であり、IPA の公式見解・公式な取り組みではなく、IPA の推薦を受けたものでもない。
---

# /system-record/instance
- 名前: ipa-josh(IPA の Japan Open Source Hub に基づく kcaim)
- 作成日: 2026-10-30
- 作成方法: AI(Claude)が、hfu の依頼に基づき、2026-10-30 に取得した公開ページ・PDF・GitHub リポジトリを読んで下書きした。人による内容確認は未了。要約と言い換えが中心で、各資料の本文は取り込んでいない。
- 位置づけ: 個人(hfu)による公開資料の整理である。IPA の公式な取り組みではなく、IPA の推薦を受けたものでもない。ハブや各資料の記述を IPA の見解として引用するときは、必ず一次資料に当たること。
- 境界づけ(範囲内): ハブの公開資料に基づく、OSS の導入・参加・組織づくり(特に OSPO の立ち上げ)に関する問い。主な読者像は、OSS の導入を進める組織の担当者、ソフトウェア開発者、OSS コミュニティの運営者。
- 範囲外: ①個別の OSS ライセンスの法的判断。②特定の OSS 製品の推奨。③ハブに載っていない他国・他機関の制度の詳細。範囲外の問いには、境界を示し、必要なら法務・専門家への相談を促す。
- 自己実行のテストの偏り: 受け入れテストは作成者(同じ AI)が自分で書いて自分で答えた。出題も採点も同じ主体なので、結果は楽観側に偏りうる。盲検の実行は別の主体が行う(`/inventory/ingest-and-backlog`)。
- 機微情報: 含まない。連絡先の値(メールアドレス・電話番号)は書かず、機能で書く。個人名は書誌情報としても省略した(登壇者・執筆者名はライブラリや各資料に記載がある)。
- 状態の語彙: `verified`(固定した出典の版にその記述があることを確かめた事実)/ `stated`(出典の主張・見解)/ `derived`(この kcaim の作り手が導いた解釈。`derives_from:` 必須)/ `normative`(規範。`authority:` 必須)/ `volatile`(`freshness:` 必須)/ `open`。`recalled` は使わない。出典を取得できなかった事項は `/open-questions` に回し、記憶で埋めない。
- 正本: この `.md` ファイル。
- 版の固定: 出典の取得日は 2026-10-30(各 `/sources/` の `fetched_at`)。スターターキットの GitHub は commit f46b52a を読んだ。

# /authorities/source-precedence
- status: normative
- authority: この kcaim の作り手(hfu)が定めた運用規則。IPA が定めたものではない。
- as_of: 2026-10-30
- 規則(優先順位の高い順):
  1. 個々の資料(PDF・資料ページ)の固定した版の本文。ライセンス・発行日・版はその資料の表記に従う。
  2. ハブの各ページの紹介文・更新履歴(資料の概要。資料本文と食い違うときは資料本文を優先する)。
  3. スターターキットのように外部リポジトリにもある資料は、読んだ commit を明記し、ページの日付とリポジトリの状態が食い違いうることを前提にする。
  4. 登壇資料は、講演時点の登壇者の見解・仮説として読む(`stated`)。レポートの結論とは区別する。
  5. この kcaim の `derived` は、いつでも上記の根拠に置き換えられるべき解釈であり、権威ではない。
- ドラフト版の扱い: 「ドラフト版」と明記された資料(OSPO スターターキット)は正式版ではない。内容は今後大幅に変わりうるので、回答には版と日付を添え、規程としてそのまま使えるかのような答えをしない。
- source: kit-page, kit-repo

# /authorities/license-labels
- status: verified, normative
- authority: 再利用の可否は、各資料に明記されたライセンスに従う(ハブのライブラリが述べている方針)。この kcaim の ライセンス(CC0)は資料の権利に及ばない。
- source: hub-library, kit-page, workbook, guidebook-biases, talk-jsconf-2025, talk-foss4g-2025-kansai
- as_of: 2026-10-30
- 確認した事実: ライブラリは、掲載資料は「明記されたライセンスに基づき」活用・転載・展開できると述べている。表記は資料ごとに異なる。スターターキットは CC0 1.0、ワークブックを含む多くは CC BY 4.0、FOSS4G 2025 KANSAI の講演資料 1 件は CC BY-SA 4.0 と表示されている。
- 確認した事実: JSConf JP 2025 の講演資料は本文が CC BY 4.0 で、図版の一部(CC BY-NC 2.5 の素材)は別条件と資料内に明記されている。
- 確認した事実: ワークブックやガイドブックの PDF には「第三者の著作権を含む部分は適用外」という趣旨の注記がある。

# /organization/ipa-units
- status: verified, volatile
- source: hub-top, hub-about, hub-library
- as_of: 2026-10-30
- freshness: 組織改編の反映が続いている。ハブの問い合わせ先表記は 2026-08 〜 09 に変わった。回答のたびにハブの現行ページで確かめる。
- 確認した事実: ハブは IPA の「デジタル基盤センター」のオープンソース推進チームが作った資料を集約する、とライブラリで述べている(ライブラリの冒頭説明)。
- 確認した事実: 各ページの問い合わせ先の部署名は「デジタル&AIシステムズ・デザインセンター」と表示されている。2026-08-01 の組織改編に伴い更新したという更新履歴がある。
- 確認した事実: 登壇資料の書誌では、登壇者の所属が「デジタル基盤センター デジタルエンジニアリング部 ソフトウェアエンジニアリンググループ」(IPA)と表記されている。
- 注意: 旧部署名と現部署名の対応関係(どの組織がどれに移ったか)を述べた記述は、読んだ範囲に見当たらない。→ `/open-questions/org-mapping`

# /organization/readers-and-actors
- status: verified, stated
- source: hub-top, hub-about, hub-adopt, kit-page, workbook, guidebook-biases
- as_of: 2026-10-30
- 確認した事実(ハブのトップ): 冒頭文は、OSS に触れるのが初めての方も、導入を進める方も、と呼びかけている。「読者像」を定義した節や一覧は、読んだ 7 つのハブのページ(トップ・IPAオープンソース推進について・OSSを知る・関わる・学ぶ・つながる・レポート・OSSに取り組む・活かす・資料公開ライブラリ)には見当たらなかった。
- 述べられていること(ハブ・IPA): OSS に関わる主体は、企業・行政機関・教育機関・開発者といったプレーヤー自身であり、IPA は自律的な行動を後押しする「伴走者」の立場で機能する(トップと「IPAオープンソース推進について」)。
- 確認した事実(資料別の対象): スターターキットは、OSPO を立ち上げたい方、社内の OSS ルールを整備したい法務・知財・セキュリティ担当者、現場に周知したいエンジニアリングマネージャーを挙げる。ワークブックは、OSPO の構築を始める企業・組織の担当者を挙げる。ガイドブックは、開発者・プロジェクト管理者・経営層・法務や人事などのコーポレート部門など「組織として OSS に関わるすべての方」を挙げる。
- 確認した事実: 読んだ範囲のハブのページに、OSS コミュニティ(プロジェクト)の運営者・メンテナーを名指しした読者区分は見当たらない。→ `/open-questions/community-operator-audience`

# /relationships/inquiry-channel
- status: verified, volatile
- source: hub-library, hub-about
- as_of: 2026-10-30
- freshness: 問い合わせ先の部署名・連絡手段は 2026-08 〜 09 に更新されている。使う直前にハブの現行ページで確かめる。期限切れ(確認から 30 日超)のときは、値を答えず、確認方法だけを答える。
- 機能での記述: IPA の問い合わせ窓口。ハブの各ページ末尾の「お問い合わせ先」の案内に従う。メールアドレスなど連絡先の値はこの kcaim に書かない(変更されたため)。
- 確認した事実: 問い合わせ先のメールアドレスは 2026-09-11 に変更されたと、複数のページの更新履歴にある。

# /relationships/ipa-stance
- status: stated
- source: hub-about
- as_of: 2026-10-30
- 述べられていること(IPA): 官民をつなぐハブ機能を中立的な立場から果たし、実践知に基づく制度設計を後押しする。OSPO 設置・調達改革・評価指標設計といった制度整備は、産業界・行政機関らの連携なしには進まないとする。
- 注意: これは IPA の自己記述であり、実際にそう機能しているかの評価ではない。

# /assets/ospo-starter-kit
- status: verified, stated, volatile
- source: kit-page, kit-repo, hub-library
- as_of: 2026-10-30
- freshness: ドラフト版で、更新される可能性が明示されている。GitHub のリポジトリはページの更新日より新しい状態でありうる(読んだ commit は 2026-10-22 付)。使う直前に版を確かめる。
- 種別: 文書テンプレート集(Markdown)。OSPO の設立・運用に使う。
- 発行者・発行日: IPA。ハブのライブラリでは発行日・掲載日とも 2026-04-16。
- ライセンス: CC0 1.0 Universal(ページ・リポジトリの LICENSE ともに確認)。
- 状態(確認した事実): ページとリポジトリの README が「ドラフト版(未完成)」と明記し、一部は検討中・作成途中で、今後大幅に更新される可能性があると述べる。
- 構成(確認した事実): A. OSS ポリシー(全社規定)テンプレート: はじめに + 第0条(前文)〜第15条(改定および施行)の条文サンプル。各条文は「条文サンプル」「解説」「カスタマイズの観点と運用上の留意事項」の3部構成。扱う論点には、OSPO、OSS の利用、コントリビューション、自社著作物の OSS 公開、従業員の私的 OSS 活動、商標、ライセンス違反・インシデント、セキュリティ・脆弱性、記録・報告、教育、就業規則との関係がある。B. 運用テンプレート(社内ポータル掲載用): 基礎・組織(6 文書)、ライセンスコンプライアンス(6 文書)、実務・OSS活用(6 文書)。担当者向けと利用者向けの使い方文書が付く。
- 入手方法: GitHub(japan-opensource-hub/ospo-starter-kit)、またはハブ上の ZIP。
- 免責(確認した事実): 一般的な雛形であり、運用にあたっては自社の法務・知財部門または専門家の確認を受けること。現状のまま提供され、無保証。
- 取り込み状況: ページ全文・リポジトリ README・使い方文書・ポリシー導入文書・OSPO 文書の冒頭を読んだ。各条文(第0〜15条)と他の運用テンプレートの本文は読んでいない。

# /assets/ospo-workbook
- status: verified, stated
- source: workbook, hub-library
- as_of: 2026-10-30
- 種別: 演習用ワークブック(PDF、約 1.1 MB)。OSPO レベル1構築ワークショップで使う。
- 発行者・発行日・ライセンス: IPA、2026-04-16、CC BY 4.0(第三者の著作権を含む部分は適用外との注記がある)。
- 構成(確認した事実): 「知る」「考える」「言語化する」を繰り返す設計。全5章で、各章に「第1段階(種をみつける)」「第2段階(言葉にする)」がある。第1章: スターターキットをベースに自社の OSS 推進計画を検討、第2章: ステークホルダーへのメリット訴求、第3章: 開発者にとってのメリット、第4章: 管理者にとってのメリット、第5章: OSPO 設置の戦略。最後のアウトプットシートは Mission / Incentive / Compliance / Engagement の4つの柱で総括する。
- 述べられていること: 高度な専門知識がなくても取り組める設計で、「分からない」という気づき自体が出発点になる。
- 取り込み状況: ハブのページ全文、PDF のライセンス表示の確認。PDF の演習ページの本文は読んでいない。

# /assets/guidebook-biases
- status: verified, stated
- source: guidebook-biases, hub-learn, hub-library
- as_of: 2026-10-30
- 種別: ガイドブック(PDF、Ver.1.0)。「その『思い込み』がリスクになる?OSSに対する誤解を解く5つの処方箋」。
- 発行者・発行日・ライセンス: IPA、2026-02-25、CC BY 4.0。
- 構成(確認した事実): 5つのバイアスと対応する「処方箋」。1 品質、2 権利(ライセンス)、3 コスト、4 キャリア、5 参加(インナーソース)。各処方箋の末尾に、経営・法務・財務・人事・組織開発などの担当者向けの要点メモが付く。
- 述べられていること(処方箋2 権利): 「Free」は無料でなく自由を意味し、自由は無条件でない。「社内ツールだから関係ない」(別法人への提供は配布とみなされうる)、「SaaS だから配布していない」(AGPL などはネットワーク経由の利用にも提供義務を課す)、「バイナリだけ渡せばよい」(GPL 系ではソースコードの提供義務がある)を代表的な誤解として挙げる。代表的なライセンス(MIT/BSD、Apache 2.0、LGPL/MPL、GPL、AGPL/SSPL)の特徴を整理し、判断に迷ったら自己判断せず OSPO や法務に相談するよう促す。
- 述べられていること(処方箋3 コスト): OSS をコスト削減でなく投資戦略として捉える。商用ソフトの OpEx に対し、OSS は自社の技術資産への投資(CapEx)に近い。BCP(ベンダー倒産・値上げへの備え)、納品物に含まれる OSS のリスト化(SBOM 等)などのサプライチェーン管理、商用ライセンスが必要なケースにも触れる。
- 述べられていること(処方箋4 キャリア): OSS 活動を「週末の趣味」でなく「平日の業務」にでき、ポータブル・スキルが身につき、採用広報や自律的な人材の育成にもなる。個人の努力でなく組織文化として取り組むことを促す。
- 述べられていること(処方箋5 参加): 英語や公開への不安には、まず社内で OSS の手法を実践するインナーソースが「安全な練習場」になる。4 つの原則(Openness、Transparency、Prioritized Mentorship、Voluntary Code Contribution)と、始める 3 ステップ(公開範囲を社内全体に広げる、README を整える、Issue で議論する)を示す。
- 取り込み状況: はじめに、対象者、目次、処方箋1〜5と要点メモの本文を読んだ(2 回目の取り込み)。あとがき・参照文献は読んでいない。

# /assets/report-2025
- status: stated, volatile
- source: report-2025, hub-report
- as_of: 2026-10-30
- freshness: 年次レポート。数値は 2025 年度の調査時点のもので、次年度版で更新される見込み。数値を答えるときは調査年度と対象(362 社など)を添える。
- 種別: 年次レポート(PDF、約 1.4 MB)。「2025年度オープンソース推進レポート:世界の潮流と日本の現在地」。
- 発行者・発行日・ライセンス: IPA、2026-05-13、CC BY 4.0(第三者の著作権部分は適用外)。
- 述べられていること(エグゼクティブサマリー): 国内企業 362 社のソフトウェア動向調査と、7 か国・30,298 リポジトリの GitHub 国際比較を統合した。OSS ポリシー整備率は 2024 年度実績 19.5%(統計的補正後 32.0%)から 2025 年度実績 36.7% へ。OSPO 設置率は 2025 年度実績 4.1%(設置済み+計画中で 6.9%)で、補正後の前年度値と比べて実質横ばいから微減とする。日本の行政 OSS は 626 件・22 組織で、「周回遅れ」ではなく「在来種型」の発展段階にあると考えられるとする。5 つの提言(OSS をデジタル主権の基盤に位置づける/政府機関・大企業・大学への OSPO 設置推進/政府 IT 調達の OSS 優先原則/重要 OSS メンテナーへの官民連携の公的支援/EU 市場向け事業組織の CRA 対応の早期着手)と、「日本型 OSS モデル」(在来種戦略・種まき戦略・Rules as Code)を示す。
- 述べられていること(4.3 持続可能性と資金調達): 多くの重要 OSS が少数のボランティア・メンテナーに支えられる「過少投資問題」を指摘する。引用された研究(Harvard Business School)による推計として、OSS がなければ企業が再開発するコストは 8.8 兆ドル、その需要側価値の 96% を 5% の開発者が生み出すとする。解決策の例として、ドイツの Sovereign Tech Fund(公的資金)、EU-STF 構想、Open Source Pledge(民間の自主的な支払い)を挙げ、日本でも官民連携の持続可能性モデルの設計が課題とする。OSS 貢献の ROI は、Linux Foundation 等の 2026-02 の報告を引いて、貢献組織の平均 2〜5 倍とする。これらの数値は引用された外部研究のもので、IPA 自身の調査結果ではない。
- 取り込み状況: 表紙・ライセンス表示・エグゼクティブサマリー・目次・第1章冒頭・4.3 節を読んだ。第2章以降の他の節の本文は読んでいない。

# /assets/report-govoss-2025
- status: stated, volatile
- source: report-govoss-2025, hub-report
- as_of: 2026-10-30
- freshness: 2026-03 時点の GitHub 上の調査。リポジトリ数などは日々変わる。調査の対象外(他プラットフォーム、政府系インナーソース)があることを添えて答える。
- 種別: 調査報告書(PDF、約 6.6 MB)とデータセット(ZIP)。「行政によるオープンソースソフトウェア公開活動の国際比較調査報告書」(世界のOSS動向レポート)。
- 発行者・発行日・ライセンス: IPA、2026-03-04、CC BY 4.0。
- 述べられていること(エグゼクティブサマリー): 日本・エストニア・シンガポール・ドイツ・フランス・英国・米国の政府・公的機関の GitHub 上の OSS を、リポジトリ数・プルリクエスト数・スター数などで分析。英国(リポジトリ約 16,000 件)と米国(約 10,000 件)は大規模、フランス(約 2,400 件)は中規模、日本(626 件、プルリクエスト約 3,800 件)・エストニア・シンガポール・ドイツは小規模と分類。政策導入の前後で公開数が増える時期的な重なりが見られるが、因果関係は明らかになっていないとする。日本は国土交通省・国土地理院の地図・空間情報分野の活動が特徴的。
- 取り込み状況: エグゼクティブサマリーと目次を読んだ。各国別・分析章の本文、付録は読んでいない。

# /assets/report-2024
- status: stated
- source: hub-library, hub-report, hub-about
- as_of: 2026-10-30
- 種別: 年次レポート(PDF)。「2024年度オープンソース推進レポート:日本におけるオープンソース戦略形成に向けた現状と展望」。
- 発行者・発行日・ライセンス: IPA、発行 2025-04-25、掲載 2025-08-08、CC BY 4.0(ライブラリの表記)。
- 述べられていること(ハブの紹介文): 2024 年度の活動を統括し、2024 年度ソフトウェア動向調査の回答分析と海外の政策事例から、日本が取り組むべき推進策を提言する。
- 取り込み状況: ハブ上の紹介文のみ。PDF は取得していない。

# /assets/talks-library
- status: verified, stated
- source: hub-library, talk-jsconf-2025, talk-osc-kyoto-2024, talk-foss4g-2025-kansai
- as_of: 2026-10-30
- 種別: 登壇資料(PDF)の集合。ライブラリの「プレゼンテーション資料」に 2025 年度 8 件・2024 年度 6 件、ほかに「思い込み」アンケートのまとめ(日本語・英語版)がある。講演の際のスライドを一部修正している場合がある、とライブラリが注記している。
- ライセンス(確認した事実): ライブラリの表記は、FOSS4G 2025 KANSAI コアデイの講演資料 1 件が CC BY-SA 4.0、ほかは CC BY 4.0。
- 2025 年度の件名(ライブラリの表記の要約): 令和の OSS のゆくえ(OSC 2026 Tokyo/Spring)/ IPA の OSPO スターターキットとワークショップ(英語、Open Compliance Summit)/ 持続可能性と世界の OSS 政策(JSConf JP 2025)/ OSPO 人材の育成(LF Japan Community Days)/ オープンソース推進レポートに見る現状と課題(アカデミック OSPO のワークショップ)/ OSS は公共財となりうるか(FOSS4G 2025 KANSAI)/ Japan Open Source Hub(英語、OpenSSF Community Day Japan 2025)/ オープンソースがもたらすインパクト(アイデアソン)。
- 2024 年度の件名: デジタル人材とオープンソース推進施策(組込みシステム関連イベント)/ オープンソースエコシステムをどのように変えていくか(OSC 2025 Tokyo/Spring)/ OSS ツッコミ想定問答集のキックオフ(Code for Japan Summit 2024)/ なぜ IPA がオープンソースを推進するのか(FOSS4G Japan 2024)/ サステナブルなコミュニティ実現に向けた私たちのオープンソース推進(OSC 2024 Kyoto)/ オープンソースは誰のため(OSS 利活用事例セミナー)。
- 取り込み状況: JSConf JP 2025 と OSC 2024 Kyoto は全スライドを読んだ。ほかは件名・概要・日付・ライセンスのみ。FOSS4G 2025 KANSAI は本文を取得していない。

# /assets/column-series
- status: verified, stated
- source: series-economic-value, hub-learn
- as_of: 2026-10-30
- 種別: 連載(Web 記事、全4回)とコラム。ハブの「OSSを知る・関わる」にある。連載「OSS/DPGs の価値を経済の言葉に翻訳する」は 2026-10-29 公開(ハブのお知らせに同日付で追加の記載)。ほかに、デジタル基盤センターのコラムが 2 本(エコシステムを循環させるイネーブラー、オープンソースエコシステムをどのように変えていくか)。
- 確認した事実: 連載のページは、内容が執筆者の見解に基づくもので、IPA の公式見解ではないという趣旨を述べている。
- 述べられていること(連載ページの紹介の要約): 第1回 OSS の価値がどこで見えなくなるか、第2回 国内外での見える化の事例、第3回 公共性ある OSS/DPGs が資金繰りでつまずきやすい理由、第4回 価値を経済の言葉に翻訳する枠組み。
- ライセンス: 連載第1回とコラム 2 本のページ本文をキーワード(ライセンス・Creative Commons・CC BY)で調べたが、Creative Commons などの表記は見当たらなかった(2 回目の取り込み)。表記がないことは、自由に使えるという意味ではない。→ `/open-questions/column-license`
- 確認した事実: コラム「オープンソースエコシステムをどのように変えていくか」(公開日 2024-12-23)のページは、執筆者の見解で IPA の公式見解ではない旨を述べる。コラム「エコシステムを循環させるイネーブラー」の公開日は 2026-02-12。
- 取り込み状況: 連載の目次ページと第1回のページ冒頭、コラム 2 本のページ冒頭とライセンス表記の有無のみ(2 回目の取り込み)。各回・各コラムの本文は読んでいない。

# /assets/ws-season1-materials
- status: verified
- source: ws-season1-archive, hub-events
- as_of: 2026-10-30
- 種別: ワークショップの記録ページと配布資料(PDF 5 点: 第1〜3回の宿題・ワークシート・ネクストアクション)、イベントの進行スライド・アンケート集計(PDF)。
- ライセンス: 記録ページは CC BY 4.0(第三者の著作権部分は適用外)。個別の PDF のライセンスは確認していない。
- 取り込み状況: 記録ページ全文を読んだ。PDF は取得していない。

# /assets/discover-biases-sheet
- status: verified
- source: hub-library
- as_of: 2026-10-30
- 種別: アンケート結果のまとめ(PDF、日本語・英語)。「これって思い込み?OSSに対するバイアスを発見しよう」。2024-11-16 の Code for Japan Summit 内セッションのリアルタイムアンケートの回答を整理したもの。掲載日 2025-08-08、CC BY 4.0(ライブラリの表記)。
- 取り込み状況: ライブラリの紹介文のみ。PDF は取得していない。

# /assets/event-code-of-conduct
- status: verified
- source: hub-events
- as_of: 2026-10-30
- 種別: IPA 主催オープンソース推進イベントの行動規範(ハブ内の独立ページ)。イベント参加は規範の遵守への同意とみなす、とイベントページが述べる。
- 取り込み状況: イベントページの紹介のみ。行動規範ページの本文は取得していない。

# /procedures/ospo-first-steps
- status: stated
- source: kit-repo, workbook
- as_of: 2026-10-30
- 述べられていること(スターターキットの OSPO 担当者向け使い方文書): 現時点で分からなくてもよい。分からない点を明確にし、誰に協力してもらうか、何を準備するかを明らかにする。完全版を目指して止まるより、最小構成で公開し、運用しながら改善する(段階的リリース)。
- 述べられていること: 最初に、OSPO が何を最優先にするか(例: コンプライアンス重視/セキュリティ重視/公開・貢献促進)を決める。論点は Mission / Incentive / Compliance / Engagement の4つの柱で点検する。
- 述べられていること: 最初に整備する項目の例は、ガイドの入り口文書、OSS の基礎・利点、OSS を使う流れ、探し方と社内導入済みリスト、評価方法、ライセンスの基礎、サプライヤーからの入手手順、FAQ・用語集、インシデント/脆弱性の報告・初動、出荷・提供前の確認(配布・提供する組織は早期に必須)。ソースコード提供義務のあるライセンスなどの注意事項は、運用が回り始めてから段階的に整備する項目に置かれている。
- 述べられていること(ワークブック): 個人で考え、チームで議論するサイクルで、自社の OSS 推進計画、ステークホルダー向けのメッセージ、OSPO 設置計画を言語化する。
- 注意: 手順の細部(担当部署の決め方、承認フロー)はキットの各文書にある可能性があるが、読んでいない。

# /procedures/oss-evaluation-three-stage
- status: stated
- source: guidebook-biases
- as_of: 2026-10-30
- 述べられていること(ガイドブック処方箋1。評価フローの「一例」と明記): 第1段階 基本チェック(ライセンスが利用形態に合うか、活発性、最低限の機能要件)、第2段階 技術的評価(実際の動作、性能・安定性、既存環境との統合性、依存関係)、第3段階 セキュリティとリスク評価(脆弱性への対応の速さと透明性、プロジェクトの持続可能性、リスクの受容と緩和)。完全な OSS はないので、判断基準は実用的・現実的に設定する、とする。
- 述べられていること: 落とし穴として、スター数への過度な依存、最新版への盲信(企業利用では LTS や Stable が定石)、必要以上に多機能な OSS を挙げる。

# /procedures/reuse-hub-material
- status: normative
- authority: この kcaim の作り手(hfu)が定めた運用規則。IPA が定めたものではない。
- source: hub-library
- as_of: 2026-10-30
- 規則: ハブの資料を転載・改変・再配布する前に、その資料のライセンス表記を現行ページと資料本体で確かめる。CC BY は出典表示(題名・発行者・ライセンス・URL)が要る。CC BY-SA は派生物にも同じ条件が及ぶので、組織の規程や商用の教材に取り込む前に法務の確認を受ける。CC0 は表示不要とされるが、出典を記すのが望ましい。第三者の著作権を含む部分(図版など)は、資料のライセンスの対象外でありうる。ライセンス表示は更新されることがある(`/traces/library-license-label-fix-2026-03-04`)。
- 注意: これは法的判断ではない。

# /decision-support/kit-as-policy
- status: derived
- derives_from: /assets/ospo-starter-kit, /authorities/source-precedence
- source: kit-page, kit-repo
- as_of: 2026-10-30
- 解釈: スターターキットのひな形は、そのまま自社の社内規程にしてはならない。根拠は3つ。①キット自身が、ドラフト版(未完成)で今後大幅に更新されうると述べている。②キット自身が、一般的な雛形であり、運用前に自社の法務・知財部門または専門家の確認を受けるよう求め、無保証としている。③ポリシーのはじめにが、たたき台であり、自社の組織形態・事業・既存規程に合わせて修正して採用するよう述べている。
- 帰結: ライセンス(CC0)上は改変・再配布に制約がないとされる。しかし、規程として採用してよいかは、ライセンスとは別の、自社の法務・組織上の判断である。
- volatile な前提: ドラフト版の状態は変わる。答えには版(commit)と日付を添える。

# /decision-support/license-question-routing
- status: normative, derived
- authority: この kcaim の作り手(hfu)が定めた運用規則。
- derives_from: /assets/ospo-starter-kit, /assets/ospo-workbook, /assets/guidebook-biases
- source: kit-page, workbook
- as_of: 2026-10-30
- 規則: 個別の OSS ライセンス(GPL など)を自社製品に組み込んでよいかという問いは、この kcaim の範囲外である。判断はしない。代わりに、①利用形態(社内利用・配布・SaaS)で義務が変わりうること(ガイドブックが述べている)、②スターターキットとワークブックがどちらも法務・知財部門または専門家の確認を求めていること、を示し、自社の法務・専門家に相談するよう促す。特定のライセンスの適否や、法的な結論を述べない。

# /decision-support/answer-quality-concern
- status: derived
- derives_from: /assets/guidebook-biases, /procedures/oss-evaluation-three-stage
- source: guidebook-biases
- as_of: 2026-10-30
- 解釈: 経営層の「OSS は品質が不安」には、ガイドブック処方箋1の論旨で答えられる。①OSS の品質は玉石混交で、無条件に信じてはならない(ガイドブックの前提)。②問題は「無料か」ではなく、評価の仕組みを持つか。③評価は3段階のフローで組織が自分で行える。④完全に安全な製品はなく、見るべきは脆弱性の有無より、修正と情報公開の速さである。
- 限界: ガイドブックは「集合知」「透明性」などの論拠を主張として述べる。これらが常に成り立つことの保証ではない。商用製品との品質の優劣を一般に述べることはできない。

# /scenarios/start-ospo
- status: derived
- derives_from: /procedures/ospo-first-steps, /assets/ospo-starter-kit, /assets/ospo-workbook
- source: kit-repo, workbook
- as_of: 2026-10-30
- 状況: 企業の担当者が、社内に OSPO を立ち上げたいが、何から始めてよいか分からない。
- 解釈(導いた答え): ①完璧を目指さず、最小構成で始める。②最優先の目的(コンプライアンス・セキュリティ・公開貢献)を決める。③ワークブックで、自社の事業・OSS の現状・ステークホルダーを言葉にする。④キットの運用テンプレートのうち、「最初に整備する項目」から自社用に直し、社内ポータルに公開する。⑤規程にあたるポリシーは、法務・知財の確認を経て採用する。

# /scenarios/quality-concern-from-executive
- status: derived
- derives_from: /decision-support/answer-quality-concern
- as_of: 2026-10-30
- 状況: 経営層から「OSS は品質が不安」と言われた。
- 解釈: `/decision-support/answer-quality-concern` の論点で、評価の仕組みを提示する。ガイドブックには経営層向けの要点メモがあるので、一次資料を示す。

# /scenarios/reuse-in-training
- status: derived
- derives_from: /procedures/reuse-hub-material, /authorities/license-labels
- source: hub-library
- as_of: 2026-10-30
- 状況: ハブの資料を自社の研修資料に転載・改変したい。
- 解釈: 資料ごとにライセンスが違うので、一括では答えられない。ライブラリの表記では、スターターキットは CC0、ワークブック・ガイドブック・レポートと多くの登壇資料は CC BY 4.0(出典表示が要る)、FOSS4G 2025 KANSAI の講演は CC BY-SA 4.0(研修資料などの派生物にも同じ条件が及ぶので、特に注意)。図版など第三者の素材は別条件でありうる。

# /scenarios/developer-first-contribution
- status: derived
- derives_from: /assets/guidebook-biases, /assets/ospo-workbook
- source: guidebook-biases, workbook
- as_of: 2026-10-30
- 状況: ソフトウェア開発者が、業務で OSS を使いはじめ、貢献もしたい。
- 事実: ハブの資料は開発者を読者に含めている。ガイドブックは対象者にエンジニア・開発者を挙げ(処方箋4・5は開発者に直接関わる)、ワークブックは第3章で開発者にとってのメリットを言語化する演習を置く。ただし、開発者個人を主な読者とする独立した手引きは、読んだ範囲に見当たらない。
- 解釈(IPA が述べたことではない): ①GitHub のコードは自由素材ではなくライセンスがあるので、利用形態(社内・配布・SaaS)に応じて確かめ、迷ったら OSPO や法務に相談する(ガイドブック処方箋2)。②採用前の評価を3段階で行う(処方箋1)。③OSS 活動は業務になりうるので、社内の OSPO やポリシーの有無を確かめ、ポータブル・スキルとして評価される可能性を踏まえる(処方箋4・ワークブック第3章)。④英語や公開への不安があれば、まず社内のインナーソースで練習する(処方箋5)。

# /scenarios/community-operator-reading
- status: derived
- derives_from: /assets/talks-library, /assets/report-2025, /organization/readers-and-actors
- source: talk-osc-kyoto-2024, talk-jsconf-2025, report-2025
- as_of: 2026-10-30
- 状況: OSS コミュニティの運営者が、ハブから運営の参考を得たい。
- 解釈(間接的な示唆。ハブは運営者を読者として直接扱っていない): 運営者に向けたまとまった手引きは、読んだ範囲のハブにはない。関連しうる資料は登壇資料である。①OSC 2024 Kyoto の講演は、コミュニティを持続可能にする要素として、オープンにやる、グローバルコミュニティを意識する、行動規範やガイドラインでガバナンスを強化する、多様性・包摂性を尊重する、を挙げ、まず行動規範とコントリビュートガイドラインを定めることを促す。②JSConf JP 2025 の講演は、OSS の持続が個人の善意に頼る構造を問題とし、「組織と制度」に移す必要を提起する。③2025 年度レポート 4.3 は、少数のボランティア・メンテナーへの依存(過少投資)と、公的資金・民間の自主的な支払いによる支援モデルを整理する。運営者にとっては、資金やスポンサーの獲得を考える際の外部の動向として読める(運営者向けの助言としては書かれていない)。

# /scenarios/license-legal-question
- status: derived
- derives_from: /decision-support/license-question-routing
- as_of: 2026-10-30
- 状況: GPL のライセンスの OSS を自社製品に組み込んでよいか知りたい。
- 解釈: 範囲外。`/decision-support/license-question-routing` に従う。

# /organization/hub-purpose
- status: verified, stated
- source: hub-top, hub-about
- as_of: 2026-10-30
- 確認した事実: ハブのトップは、ハブ自身を「オープンソースの価値をひらき、つながり、育てるための入り口」と説明し、OSS に触れるのが初めての方も導入を進める方も次の一歩を見つけられるように、と呼びかけている。
- 述べられていること(IPA): IPA は日本社会全体の OSS への参加力・活用力を底上げする中核的な推進主体として、OSS を創造し、育て、支える文化の醸成・制度の設計・人材の育成に寄与することを使命とする。OSS を技術的自立とソフトウェアモダナイゼーションの基盤と位置づけ、OSS を「共創のインフラ」と呼ぶ。
- 述べられていること(課題認識): 日本では OSS への不安や誤解が根強く、関わり方が受動的にとどまる。2024 年度ソフトウェア動向調査で、企業の 8 割以上が OSS に関するガバナンス体制を持たないという趣旨の結果が出たとする。
- 述べられていること(2025 年度の目標): ビルディングブロック型開発に向けたモデル検討と部品化基盤の構築、OSS リテラシーと実践スキルに関する人材育成・教育体制の整備。2026 年度以降は、ガバナンス体制(OSPO)、エコシステムへの還元文化、公共調達での OSS の制度化に本格的に取り組む予定とする。
- 注意: 目的の記述は IPA の自己説明である。成果の評価ではない。

# /organization/hub-structure
- status: verified, volatile
- source: hub-top
- as_of: 2026-10-30
- freshness: 公開予定の項目が追加されうる。使う直前にトップページのメニューを確かめる。
- 確認した事実: トップのメニューは次のとおり。IPAオープンソース推進について/OSSを知る・関わる/レポート:調査と考察/OSSに取り組む・活かす/OSSでつくる・育てる/学ぶ・つながる/実践のストーリー/資料公開ライブラリ。このうち「OSSでつくる・育てる」と「実践のストーリー」には「後日公開予定」と表示されている。
- 述べられていること: 「OSSでつくる・育てる」は、OSS を再利用可能な部品として活用し、開発・改善・保守に参加しながらシステムを組み立てるための情報を提供するもの、「実践のストーリー」は、OSS を使い、育て、支える現場の声を集めるもの、と紹介されている。

# /traces/hub-about-published-2025-06-17
- status: verified
- source: hub-about, hub-learn, hub-events
- as_of: 2026-10-30
- 事実: 「IPAオープンソース推進について」「OSSを知る・関わる」「学ぶ・つながる」の公開日は 2025-06-17。

# /traces/library-launched-2025-08-08
- status: verified
- source: hub-library
- as_of: 2026-10-30
- 事実: 資料公開ライブラリの公開日は 2025-08-08。同日に、過去の発表資料やレポートの多くが掲載された(掲載日の表記による)。

# /traces/guidebook-published-2026-02-25
- status: verified
- source: hub-library, hub-learn, guidebook-biases
- as_of: 2026-10-30
- 事実: ガイドブック「OSSに対する誤解を解く5つの処方箋」が 2026-02-25 に追加された(Ver.1.0 初版、改訂履歴は 1 行)。

# /traces/library-license-label-fix-2026-03-04
- status: verified
- source: hub-library
- as_of: 2026-10-30
- 事実: 2026-03-04 の更新で、ライブラリはレポートを追加し、次の 3 つの登壇資料のライセンス表示(P2)の内容を修正した。OSPO 人材の育成(LF Japan Community Days)/ 持続可能性と世界の OSS 政策(JSConf JP 2025)/ OSPO スターターキットとワークショップ(Open Compliance Summit、英語)。
- 事実でないこと(不明): どう修正されたか(修正前の表示)は、読んだ範囲にない。→ `/open-questions/license-fix-detail`

# /traces/kit-and-workbook-published-2026-04-16
- status: verified
- source: hub-adopt, kit-page, workbook, hub-top
- as_of: 2026-10-30
- 事実: 「OSSに取り組む・活かす」が 2026-04-16 に公開され、OSPO スターターキット ドラフト版とワークブックが追加された。

# /traces/report-2025-added-2026-05-13
- status: verified
- source: hub-top, hub-report, hub-about
- as_of: 2026-10-30
- 事実: 「2025年度オープンソース推進レポート:世界の潮流と日本の現在地」が 2026-05-13 に追加された(PDF の日付も同じ)。

# /traces/org-reform-2026-08-01
- status: verified, volatile
- source: hub-about, hub-learn, hub-report, hub-library, kit-page
- as_of: 2026-10-30
- freshness: 組織改編の影響が続く。問い合わせ先の表記は今後も変わりうる。
- 事実: 2026-08-01 の組織改編に伴い、問い合わせ先の部署名が更新された。更新履歴の日付はページにより異なる。「IPAオープンソース推進について」「OSSを知る・関わる」「レポート」では 2026-08-03。「資料公開ライブラリ」と「スターターキット」では 2026-09-11 の項に同趣旨の記載がある。
- 解釈の保留: ページ間の日付の違いが、更新の時期の違いか、記載の仕方の違いかは分からない。→ `/open-questions/org-reform-date-mismatch`

# /traces/contact-mail-change-2026-09-11
- status: verified
- source: hub-about, hub-learn, hub-report
- as_of: 2026-10-30
- 事実: 2026-09-11 に、問い合わせ先のメールアドレスが変更された(3 ページの更新履歴)。値はこの kcaim に書かない。

# /traces/economic-series-added-2026-10-29
- status: verified
- source: hub-top, hub-learn, series-economic-value
- as_of: 2026-10-30
- 事実: 2026-10-29 に、「OSSを知る・関わる」に連載「OSS/DPGs の価値を経済の言葉に翻訳する(全4回)」が追加された。トップの「最新のお知らせ」の筆頭。

# /traces/ws-season1-held
- status: verified
- source: ws-season1-archive, hub-events
- as_of: 2026-10-30
- 事実: OSPO レベル1構築ワークショップのシーズン1は、2025 年 11 月から 2026 年 1 月にかけて全 3 回(第1回 OSPO の体制づくり、第2回 ポリシー編1 OSS ライセンス、第3回 ポリシー編2 OSS 利用における評価と実践)。成果発表会は 2026-04-17。ハブの「学ぶ・つながる」には、読んだ時点で参加募集中のイベントはなかった。

# /traces/kit-repo-ahead-of-page
- status: verified
- source: kit-page, kit-repo
- as_of: 2026-10-30
- 事実: スターターキットのページの最終更新日は 2026-09-11。取得したリポジトリの最新 commit(f46b52a)の日付は 2026-10-22。ページとリポジトリの更新時期が一致しない。

# /lessons/license-per-item
- status: derived
- derives_from: /traces/library-license-label-fix-2026-03-04, /authorities/license-labels
- source: hub-library
- as_of: 2026-10-30
- 教訓: ライセンスは資料ごとに違い、表示が後から修正されることがある。再利用の前に、ライブラリのページと資料本体の両方で確かめる。一括の答え(「ハブの資料は CC BY」など)をしない。

# /lessons/contact-by-function
- status: derived
- derives_from: /traces/org-reform-2026-08-01, /traces/contact-mail-change-2026-09-11
- source: hub-library
- as_of: 2026-10-30
- 教訓: 部署名と連絡手段は 2 か月のうちに少なくとも 2 回更新された。連絡先は値でなく機能で記し、答える直前に現行ページで確かめる。

# /lessons/page-vs-repo
- status: derived
- derives_from: /traces/kit-repo-ahead-of-page
- source: kit-page, kit-repo
- as_of: 2026-10-30
- 教訓: 外部リポジトリにもある資料は、ページの更新日とリポジトリの状態がずれる。読んだ commit を記録し、「最新」と断定しない。

# /lessons/hub-is-growing
- status: derived
- derives_from: /organization/hub-structure, /traces/economic-series-added-2026-10-29, /traces/kit-and-workbook-published-2026-04-16
- source: hub-top
- as_of: 2026-10-30
- 教訓: ハブは公開途上である(公開予定のメニュー、ドラフト版の資料、直近の追加)。「ハブにこの内容はない」は、読んだ日付の時点の事実としてのみ言える。

# /open-questions/org-mapping
- status: open
- as_of: 2026-10-30
- 問い: 旧「デジタル基盤センター」とその「オープンソース推進チーム」は、2026-08-01 の改編後のどの組織にあたるか。
- 次の行動: IPA の組織紹介ページ(ハブの外)を確かめる。人への確認が要るなら、問い合わせ窓口に尋ねる。

# /open-questions/org-reform-date-mismatch
- status: open
- as_of: 2026-10-30
- 問い: 組織改編に伴う問い合わせ先の更新は、ページにより 2026-08-03 と 2026-09-11 の両方に現れる。何がいつ反映されたか。

# /open-questions/community-operator-audience
- status: open
- as_of: 2026-10-30
- 問い: ハブは OSS コミュニティの運営者・メンテナーを読者として扱う予定か。読んだ範囲に直接の言及はない。未取得のコラム 2 本や、公開予定のメニューに含まれるかもしれない。
- 次の行動: コラム 2 本(エコシステムを循環させるイネーブラー/オープンソースエコシステムをどのように変えていくか)を取得して確かめる。

# /open-questions/coming-soon-menus
- status: open, volatile
- freshness: 公開されたら即時に変わる。
- as_of: 2026-10-30
- 問い: 「OSSでつくる・育てる」「実践のストーリー」の内容と公開時期。ハブは「後日公開予定」とだけ述べている。

# /open-questions/license-fix-detail
- status: open
- as_of: 2026-10-30
- 問い: 2026-03-04 の 3 資料のライセンス表示(P2)の修正は、何をどう変えたか。現在の PDF のライセンス表示(CC BY 4.0 + 一部素材は別条件)が修正後のものと考えられるが、修正前は未確認。

# /open-questions/column-license
- status: open
- as_of: 2026-10-30
- 問い: 連載(全4回)とコラム 2 本の、ライセンス。読んだページ本文に表記は見当たらなかった。連載は執筆者の見解で IPA の公式見解ではないとされているため、扱いも別でありうる。ページ末尾やサイト共通の利用条件にあるかは未確認。

# /open-questions/report-body-unread
- status: open
- as_of: 2026-10-30
- 問い: 2025 年度レポートの第2章以降(企業調査の詳細、持続可能性と資金調達の節 4.3、提言の詳細)と、行政 OSS 調査の本文の内容。エグゼクティブサマリーだけを読んだので、数値の定義や調査の限界を確かめていない。

# /open-questions/foss4g-sa-content
- status: open
- as_of: 2026-10-30
- 問い: FOSS4G 2025 KANSAI の講演資料(CC BY-SA 4.0)の内容。意図的に取り込まなかった。概要は「OSS は公共財となりうるか」と国の OSS 戦略、デジタル公共財の概念(ライブラリの紹介文)。

# /open-questions/kit-releases
- status: open, volatile
- freshness: リポジトリの更新に応じて変わる。
- as_of: 2026-10-30
- 問い: スターターキットの正式版の予定、リリースの履歴(README は Releases を参照するよう案内している)。

# /open-questions/pdf-attachments-unread
- status: open
- as_of: 2026-10-30
- 問い: ワークショップの配布資料 5 点、成果発表会のスライドとアンケート集計、事前説明会の資料、「思い込み」アンケートのまとめ、2024 年度レポートの本文の内容。取得していない。

# /acceptance-tests/hub-purpose
- query: このハブの目的は何か。
- scope: 範囲内
- expected: ハブ自身が「OSS の価値をひらき、つながり、育てるための入り口」と述べること(述べられていること)と、それがトップページと「IPAオープンソース推進について」に載っていること(確認した事実)を分けて答える。IPA の使命(参加力・活用力の底上げ、伴走者)も述べられていること。自己説明であり成果の評価ではないと添える。
- requires: /organization/hub-purpose, /organization/readers-and-actors
- result: pass
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: なし
- missing_source_limit: ハブの目的に対する成果の評価は出典にない。
- freshness: ハブの文言は変わりうる。読んだ日(2026-10-30)を添える。

# /acceptance-tests/hub-audience
- query: このハブの対象読者は誰か。
- scope: 範囲内
- expected: ハブは読者像を明示的に定義した節を持つとは確認できない(読んだ 7 ページの範囲)。トップの呼びかけは、初めての方と導入を進める方。関わる主体として企業・行政機関・教育機関・開発者を挙げ、IPA は伴走者とする。資料ごとの対象(キット、ワークブック、ガイドブック)は別に明示されている。
- requires: /organization/readers-and-actors
- result: pass
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: 公開予定のメニューや未取得のコラムにある読者の記述。
- missing_source_limit: ハブ全体としての読者定義は、読んだ範囲に存在しない。
- freshness: ハブが更新されると変わる。

# /acceptance-tests/implications-for-developers
- query: このハブは、ソフトウェア開発者に何を示唆するか。
- scope: 範囲内
- expected: IPA が述べたことと、作り手が導いた解釈を分ける。ガイドブックとワークブックが開発者を読者に含めていることを事実として述べる(独立した個人向け手引きは見当たらない)。そのうえで、ライセンスの確認、採用前の評価、社内の OSPO/ポリシーの確認、インナーソースを入口にすること、を「導いた示唆」として示す。
- requires: /scenarios/developer-first-contribution, /assets/guidebook-biases, /procedures/oss-evaluation-three-stage
- result: pass
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: ワークブック第3章の PDF 本文。(初回の自己実行ではガイドブック処方箋2〜5の本文が未取り込みで partial だった。2 回目で取り込み済み。)
- missing_source_limit: 開発者個人を主な読者とする独立した手引きがハブにあるかは、読んだ範囲では確認できない。
- freshness: ハブが更新されると変わる。

# /acceptance-tests/implications-for-community-operators
- query: このハブは、OSS コミュニティの運営者に何を示唆するか。
- scope: 範囲内
- expected: ハブが運営者を読者として直接扱っていないことを事実として述べる。関連する資料(OSC 2024 Kyoto、JSConf JP 2025 の登壇資料)から導いた示唆を、「間接的な示唆」と明記して示す。IPA の公式見解として述べない。
- requires: /scenarios/community-operator-reading, /open-questions/community-operator-audience
- result: partial
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: コラム 2 本の本文(2 回目の取り込み後も未読)。2025 年度レポート 4.3 は 2 回目で取り込み済み。
- missing_source_limit: 運営者向けの直接の記述は、読んだ範囲にない。
- freshness: ハブが更新されると変わる。

# /acceptance-tests/what-is-ospo-and-why
- query: OSPO とは何か、なぜ必要とされているか。
- scope: 範囲内
- expected: OSPO は、組織が OSS を効果的かつ安全に活用・管理・貢献するための専門部署やチーム(ワークショップ記録・ガイドブックの定義)。必要とされる理由として IPA が述べるのは、企業の 8 割以上が OSS ガバナンス体制を持たない(2024 年度調査)ことなど。2025 年度レポートは OSPO 設置率 4.1% を示す(volatile)。
- requires: /organization/hub-purpose, /assets/report-2025, /assets/ospo-workbook
- result: pass
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: スターターキットの「OSPOとは」の本文全体。
- missing_source_limit: OSPO の効果を実証したデータは、読んだ範囲にない。
- freshness: 調査数値は年次で更新される。

# /acceptance-tests/ospo-first-step
- query: OSPO を立ち上げるときの最初の一歩は何か。
- scope: 範囲内
- expected: 完璧を目指さず最小構成で始める。最優先の目的を決める。ワークブックで自社の OSS 活用を言語化する。スターターキットの「最初に整備する項目」から自社用に直す。キットはドラフト版で、規程化には法務確認が要る。
- requires: /procedures/ospo-first-steps, /scenarios/start-ospo, /assets/ospo-starter-kit, /assets/ospo-workbook
- result: pass
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: ワークブック PDF の演習ページ本文、キットの各条文。
- missing_source_limit: 組織規模ごとの具体的な手順は出典にない。
- freshness: キットはドラフト版で更新される。版(commit)を添える。

# /acceptance-tests/executive-quality-concern
- query: 経営層の「OSS は品質が不安」にどう答えるか。
- scope: 範囲内
- expected: ガイドブック処方箋1の論旨。OSS の品質は玉石混交であり、無条件に信じない。評価の仕組みを持つこと、3段階の評価、脆弱性は有無でなく対応の速さを見る、を示す。一次資料(ガイドブック)を示す。
- requires: /decision-support/answer-quality-concern, /procedures/oss-evaluation-three-stage
- result: pass
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: 処方箋3(コスト)など、経営層向けのほかの論点。
- missing_source_limit: OSS と商用製品の品質を一般に比較したデータは、読んだ範囲にない。
- freshness: ガイドブックは Ver.1.0。改訂されうる。

# /acceptance-tests/japan-oss-status-international
- query: 日本の OSS 活用の現状は、国際比較でどう見えるか。
- scope: 範囲内
- expected: 2025 年度レポートが述べる数値(ポリシー整備率 36.7%、OSPO 設置率 4.1% など、調査年度と対象を添える)と、7 か国比較で日本の行政 OSS が 626 件・22 組織で「在来種型」の発展段階にあるという解釈。数値は調査時点のもので、最新とは限らないと添える。
- requires: /assets/report-2025, /assets/report-govoss-2025
- result: volatile
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: レポート第2〜3章の定義・補正方法、第4章の国際比較。
- missing_source_limit: 民間企業の国際比較は、読んだ範囲の出典にない(比較は主に行政 OSS)。
- freshness: 年次で更新される。答えには調査年度を必ず添える。

# /acceptance-tests/government-oss-vs-other-countries
- query: 行政の OSS 公開は、他国と比べてどうか。
- scope: 範囲内
- expected: 7 か国の GitHub 調査で、英国(約 16,000 件)・米国(約 10,000 件)が大規模、フランスが中規模、日本(626 件)・エストニア・シンガポール・ドイツが小規模。日本は地図・空間情報分野が特徴的。GitHub 上のみの調査で、因果関係は未解明。
- requires: /assets/report-govoss-2025
- result: partial
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: 国別の詳細と分析章、Threats to Validity の付録。
- missing_source_limit: GitHub 以外のプラットフォームや政府系インナーソースは調査の対象外。
- freshness: 2026-03 時点の調査。リポジトリ数は変わる。

# /acceptance-tests/starter-kit-as-policy
- query: スターターキットのひな形は、そのまま社内規程にしてよいか。
- scope: 範囲内
- expected: そのままは不可。ドラフト版(未完成)で更新されうる、一般的な雛形で法務・知財等の確認が必要、はじめににも「たたき台」とある。CC0 により改変・再配布に著作権上の制約はないとされるが、規程としての採用は別の判断。
- requires: /decision-support/kit-as-policy, /assets/ospo-starter-kit
- result: volatile
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: 各条文の解説・カスタマイズの観点。
- missing_source_limit: 自社の法務判断は出典にない。
- freshness: ドラフト版の状態が変わると答えも変わる。版(commit)と日付を添える。正式版が出たら再確認する。

# /acceptance-tests/reuse-in-training-material
- query: ハブの資料を、自社の研修資料に転載・改変してよいか。
- scope: 範囲内
- expected: 資料ごとのライセンスによる。スターターキット CC0、ワークブック・ガイドブック・レポートと多くの登壇資料は CC BY 4.0(出典表示が要る)、FOSS4G 2025 KANSAI の講演は CC BY-SA 4.0(派生物に同じ条件が及ぶ)。図版など第三者の素材は別条件でありうる。連載・コラムは未確認と明示する。法的判断ではない。
- requires: /procedures/reuse-hub-material, /authorities/license-labels, /scenarios/reuse-in-training
- result: partial
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: イベントスライド・ワークショップ配布資料のライセンス表記。連載・コラムは、ページ本文に表記が見当たらない(2 回目の取り込み後)ので、問い合わせか確認が要ると答える。
- missing_source_limit: 個別の利用が条件を満たすかの法的判断は出典にない。
- freshness: ライセンス表示は修正されることがある(2026-03-04 の例)。利用の直前に確かめる。

# /acceptance-tests/gpl-in-own-product
- query: 個別の OSS ライセンス(GPL など)を自社製品に組み込んでよいか。
- scope: 範囲外(示唆あり)
- expected: この kcaim は個別のライセンスの法的判断をしない。利用形態(社内・配布・SaaS)で義務が変わりうること、キットとワークブックが法務・専門家の確認を求めていることを示し、自社の法務や専門家への相談を促す。
- requires: /decision-support/license-question-routing, /scenarios/license-legal-question
- result: pass
- boundary: 正しく示せた。可否の結論を述べず、相談先(法務・知財・専門家)と、判断に影響する要素(利用形態)だけを示した。
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: ガイドブック処方箋2の後半(ライセンスの探し方・代表的なライセンス)。ただし範囲外なので結論には使わない。
- missing_source_limit: 個別のライセンスの法的解釈は出典にない。
- freshness: 変わりにくい。

# /acceptance-tests/community-sustainability-points
- query: OSS コミュニティの持続可能性について、IPA が示している論点は何か。
- scope: 範囲内
- expected: 登壇資料(IPA 職員による講演)が述べる論点として、OSC 2024 Kyoto: コミュニティの悲劇の連鎖(資金・人的資源の不足など)、持続させる要素(オープンにやる、グローバルを意識、ガバナンス強化、多様性・包摂性)、まず行動規範とコントリビュートガイドライン。JSConf JP 2025: 個人の善意への依存、Log4j の例、EU のクリティカル OSS 調査(FOSSEPS)、ドイツの Sovereign Tech Fund、日本の制度設計の必要。加えて 2025 年度レポート 4.3 の過少投資問題と資金調達モデル(STF、Open Source Pledge)。講演者の見解・仮説と、レポートの記述を区別する。
- requires: /scenarios/community-operator-reading, /assets/talks-library, /assets/report-2025
- result: pass
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: コラム 2 本の本文、レポートのデジタル主権の章。
- missing_source_limit: 登壇資料は議論の導入であり、IPA の公式な方針ではない。
- freshness: 講演時点(2024-07、2025-11)の内容。

# /acceptance-tests/oss-tsukuru-sodateru-content
- query: 「OSSでつくる・育てる」の内容は何か。
- scope: 範囲内
- expected: 現時点では「後日公開予定」で、内容は公開されていない。ハブの紹介文(再利用可能な部品として活用し、開発・改善・保守に参加しながらシステムを組み立てる情報を提供する)以上のことは答えられない。
- requires: /organization/hub-structure, /open-questions/coming-soon-menus
- result: fail
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: なし(取り込めるものが存在しない)。
- missing_source_limit: 出典自体が内容を持たない(公開予定)。
- freshness: 公開されたら答えが変わる。2026-10-30 時点。

# /acceptance-tests/inquiry-contact
- query: IPA への問い合わせ先はどこか。
- scope: 範囲内
- expected: 機能で答える。IPA の問い合わせ窓口で、ハブの各ページ末尾の「お問い合わせ先」の案内に従う。部署名とメールアドレスは 2026-08 〜 09 に更新されており、値はこの kcaim に書かない。現行ページで確かめるよう案内する。
- requires: /relationships/inquiry-channel, /traces/org-reform-2026-08-01
- result: volatile
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: なし
- missing_source_limit: 将来の問い合わせ先は出典にない。
- freshness: 確認から 30 日で期限切れ。期限切れのときは、値を答えず確認方法だけを答える。

# /acceptance-tests/license-label-correction
- query: ハブの資料のライセンス表示は、いつ、どの資料で修正されたか。
- scope: 範囲内
- expected: 2026-03-04 に、3 つの登壇資料(OSPO 人材の育成、持続可能性と世界の OSS 政策、OSPO スターターキットとワークショップ(英語))のライセンス表示(P2)が修正された。修正の中身は不明。
- requires: /traces/library-license-label-fix-2026-03-04, /open-questions/license-fix-detail
- result: pass
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: 修正前の表示(出典なし)。
- missing_source_limit: 出典は修正の事実を述べるのみで、中身を述べていない。
- freshness: 履歴は変わらないが、以降の修正が追加されうる。

# /acceptance-tests/choose-database
- query: 業務データベースにどの OSS を選ぶべきか。
- scope: 範囲外(示唆なし)
- expected: 特定の OSS 製品は推奨しない。範囲外であることを述べる。
- requires: /system-record/instance
- result: pass
- boundary: 正しく示せた。製品名を挙げず、範囲外とした。
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: なし
- missing_source_limit: 製品の選定は出典の対象外。
- freshness: 変わりにくい。

# /sources/hub-top
- status: verified
- title: Japan Open Source Hub(トップページ)
- issuer: 独立行政法人情報処理推進機構(IPA)
- published: 不明(ページに公開日の表記なし)。最新のお知らせは 2026-10-29
- url: https://www.ipa.go.jp/digital/kaihatsu/oss/index.html
- license: ページ単位のライセンス表記は確認していない
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 取り込み済み
- notes: 全文を読んだ。メニュー構成、お知らせ、公開予定の表示を根拠にした。

# /sources/hub-about
- status: verified
- title: IPAオープンソース推進について | Japan Open Source Hub
- issuer: IPA
- published: 2025-06-17(最終更新 2026-09-11)
- url: https://www.ipa.go.jp/digital/kaihatsu/oss/about/index.html
- license: ページ単位のライセンス表記は確認していない
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 取り込み済み
- notes: 背景、現状と課題、2025 年度の目標と計画、2026 年度以降の予定、更新履歴を読んだ。付録のアンケート結果は画像で、読んでいない。

# /sources/hub-learn
- status: verified
- title: OSSを知る・関わる | Japan Open Source Hub
- issuer: IPA
- published: 2025-06-17(最終更新 2026-10-29)
- url: https://www.ipa.go.jp/digital/kaihatsu/oss/learn/index.html
- license: ページ単位のライセンス表記は確認していない
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 取り込み済み
- notes: ガイドブック、連載、コラム 2 本の一覧と更新履歴。

# /sources/hub-events
- status: verified
- title: 学ぶ・つながる | Japan Open Source Hub
- issuer: IPA
- published: 2025-06-17(最終更新 2026-09-11)
- url: https://www.ipa.go.jp/digital/kaihatsu/oss/events/index.html
- license: ページ単位のライセンス表記は確認していない
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 取り込み済み
- notes: イベント一覧、行動規範へのリンク、アーカイブの資料リンク。参加募集中のイベントはなかった。

# /sources/hub-report
- status: verified
- title: レポート:調査と考察 | Japan Open Source Hub
- issuer: IPA
- published: 2026-03-04(最終更新 2026-09-11)
- url: https://www.ipa.go.jp/digital/kaihatsu/oss/report/index.html
- license: ページ単位のライセンス表記は確認していない
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 取り込み済み
- notes: 年次レポート 2 件と行政 OSS 調査の紹介。サブページ(2025 年度レポート、行政 OSS 調査)の概要も確認した。

# /sources/hub-adopt
- status: verified
- title: OSSに取り組む・活かす | Japan Open Source Hub
- issuer: IPA
- published: 2026-04-16(最終更新 2026-09-11)
- url: https://www.ipa.go.jp/digital/kaihatsu/oss/adopt/index.html
- license: ページ単位のライセンス表記は確認していない
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 取り込み済み
- notes: スターターキットとワークブックへの案内。

# /sources/hub-library
- status: verified
- title: 資料公開ライブラリ | Japan Open Source Hub
- issuer: IPA
- published: 2025-08-08(最終更新 2026-09-11)
- url: https://www.ipa.go.jp/digital/kaihatsu/oss/library.html
- license: 各資料に明記(ページ冒頭に、明記されたライセンスに基づき活用・転載・展開できるとの方針)
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 取り込み済み
- notes: 全文を読んだ。資料ごとの発行日・掲載日・ライセンス表記と、更新履歴の根拠。

# /sources/kit-page
- status: verified
- title: OSPOスターターキット ドラフト版(ハブのページ)
- issuer: IPA
- published: 2026-04-16(最終更新 2026-09-11)
- url: https://www.ipa.go.jp/digital/kaihatsu/oss/adopt/ospo-starter-kit.html
- license: CC0 1.0 Universal
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 取り込み済み
- notes: 全文を読んだ。ドラフト版の注意、収録内容、ライセンス、免責。制作に携わった個人の名前はページにあるが、この kcaim には書かない。

# /sources/kit-repo
- status: verified
- title: ospo-starter-kit(GitHub リポジトリ。IPA 公式の表記)
- issuer: IPA
- published: 不明。読んだ commit f46b52a は 2026-10-22 付
- url: https://github.com/japan-opensource-hub/ospo-starter-kit
- license: CC0 1.0 Universal(リポジトリの LICENSE の全文を確認)
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- notes: 浅い clone で取得。README、運用テンプレートの使い方、ポリシーのはじめに、OSPO 文書の冒頭を読んだ。条文 0〜15 とほかの運用テンプレートは未読。

# /sources/workbook
- status: verified
- title: OSPOレベル1構築ワークショップ ワークブック
- issuer: IPA
- published: 2026-04-16(ページの最終更新 2026-09-11)
- url: https://www.ipa.go.jp/digital/kaihatsu/oss/adopt/workbook-for-ospo-lv1-workshop.html
- license: CC BY 4.0(ページと PDF の表示を確認。第三者の著作権部分は適用外)
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- notes: ページ全文を読んだ。PDF(.../adopt/rcu1hd000000h5jo-att/workbook-for-ospo-lv1-workshop.pdf)を取得し、ライセンス表示を確認したが、演習ページの本文は読んでいない。CC BY の資料を要約しているので、題名・発行者・ライセンス・URL をここに残す。

# /sources/ws-season1-archive
- status: verified
- title: OSPOレベル1構築ワークショップ(全3回)シーズン1の記録
- issuer: IPA
- published: 2026-04-16(最終更新 2026-09-11)
- url: https://www.ipa.go.jp/digital/kaihatsu/oss/events/ospo-lv1-ws-season1-archive.html
- license: CC BY 4.0(ページの表示。第三者の著作権部分は適用外)
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 取り込み済み
- notes: ページ全文を読んだ。ゲスト講師は組織名・役職でなく個人名で紹介されているが、この kcaim には書かない。配布資料 PDF 5 点は未取得。

# /sources/guidebook-biases
- status: verified
- title: その「思い込み」がリスクになる?OSSに対する誤解を解く5つの処方箋(ガイドブック Ver.1.0)
- issuer: IPA
- published: 2026-02-25
- url: https://www.ipa.go.jp/digital/kaihatsu/oss/rcu1hd0000003oxl-att/guidebook-overcoming-biases-to-oss.pdf
- license: CC BY 4.0(PDF の奥付の表示とライブラリの表記)
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- notes: PDF 38 ページ。pdftotext で抽出した(一部の語に字形の置換があり、本文の誤りとは断定しない)。ハブのページ(.../learn/guidebook-biases-to-oss/index.html)でも冒頭部分を確認した。要約を載せているので、CC BY の表示として題名・発行者・ライセンス・URL を残す。

# /sources/report-2025
- status: verified
- title: 2025年度オープンソース推進レポート:世界の潮流と日本の現在地(AI・デジタル主権時代のオープンソースエコシステムの再設計)
- issuer: IPA
- published: 2026-05-13
- url: https://www.ipa.go.jp/digital/kaihatsu/oss/report/report2025/rcu1hd000000opqm-att/open-source-report2025.pdf
- license: CC BY 4.0(表紙裏の表示。第三者の著作権部分は適用外)
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- notes: エグゼクティブサマリー・目次・第1章冒頭を読んだ。ハブのページ(.../report/report2025/index.html)にも同じ要約がある。要約を載せているので、CC BY の表示として題名・発行者・ライセンス・URL を残す。

# /sources/report-govoss-2025
- status: verified
- title: 世界のOSS動向レポート:行政によるオープンソースソフトウェア公開活動の国際比較調査報告書
- issuer: IPA
- published: 2026-03-04
- url: https://www.ipa.go.jp/digital/kaihatsu/oss/rcu1hd0000005mso-att/gov-oss-github-analysis-2025.pdf
- license: CC BY 4.0(ライブラリの表記と、PDF 末尾の表示の両方を確認)
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- notes: エグゼクティブサマリーと目次を読んだ。データセット(ZIP)は未取得。ハブのページは .../report/govoss_report_2025/index.html。

# /sources/talk-jsconf-2025
- status: verified
- title: "善意"だけでは続かない ー持続可能性の問題に取り組む世界のOSS政策の話(JSConf JP 2025、2025-11-16)
- issuer: IPA(デジタル基盤センター所属の登壇者)
- published: 掲載 2025-11-18
- url: https://www.ipa.go.jp/digital/kaihatsu/oss/j5u9nn000000i4c4-att/oss-presentation-20251116.pdf
- license: 本文 CC BY 4.0。図版の一部(CC BY-NC 2.5 の素材)は別条件(資料内の表示)
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 取り込み済み
- notes: 全スライドを読んだ。ライセンス表示(P2)は 2026-03-04 に修正された資料の 1 つ。講演者の見解として扱う。要約を載せているので、題名・発行者・ライセンス・URL を残す。

# /sources/talk-osc-kyoto-2024
- status: verified
- title: サステナブルなコミュニティ実現に向けた私たちのオープンソース推進(Open Source Conference 2024 Kyoto、2024-07-27)
- issuer: IPA(デジタル基盤センター所属の登壇者)
- published: 掲載 2025-08-08
- url: https://www.ipa.go.jp/digital/kaihatsu/oss/j5u9nn0000001o4s-att/oss-presentation-20240727.pdf
- license: CC BY 4.0(資料内の表示)
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 取り込み済み
- notes: 全スライドを読んだ。2025 年に公開された資料で、講演時点(2024-07)の内容。要約を載せているので、題名・発行者・ライセンス・URL を残す。

# /sources/talk-foss4g-2025-kansai
- status: verified
- title: OSSは公共財となりうるか?IPAオープンソース推進レポートに見る日本のオープンソース戦略の現在と未来(FOSS4G 2025 KANSAI コアデイ、2025-07-05)
- issuer: IPA(登壇者所属)。イベント主催: 一般社団法人OSGeo日本支部
- published: 掲載 2025-08-08
- url: https://www.ipa.go.jp/digital/kaihatsu/oss/j5u9nn0000001o1o-att/oss-presentation-20250705.pdf
- license: CC BY-SA 4.0(ライブラリの表記)
- license_checked_at: 2026-10-30
- fetched_at: 未取得(本文を取得していない)
- ingest: 未取り込み
- notes: CC BY-SA の資料のため、本文を取り込まない方針。書誌とライセンスだけを記録する。ライブラリの紹介文の要旨は /assets/talks-library にある。

# /sources/series-economic-value
- status: verified
- title: 連載:OSS/DPGsの価値を経済の言葉に翻訳する(全4回)(目次ページ)
- issuer: IPA(執筆は外部の執筆者。ページは、執筆者の見解で IPA の公式見解ではないと述べる)
- published: 2026-10-29
- url: https://www.ipa.go.jp/digital/kaihatsu/oss/learn/economic-value-of-oss/index.html
- license: 確認していない(ページに表示があるか未確認)
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- notes: 目次ページのみ。各回の本文は未取得。

# /authorities/external-literature-handling
- status: normative
- authority: この kcaim の作り手(hfu)が定めた運用規則。IPA が定めたものではない。
- as_of: 2026-10-30
- 規則: ①josh の資料が紹介している文献(`introduced_by:` に josh の出典 id があるもの)と、紹介していない文献(読んだ範囲に紹介が見当たらないもの)を、必ず区別して示す。②外部文献を勧めることは、IPA がそれを推薦していることを意味しない。選定は作り手(AI)の判断で、人の確認は未了。③外部文献の本文は取り込まず、書誌・ライセンス表記・読んだ範囲・短い要約にとどめる。④外部文献のライセンスは josh の資料と別であり、資料ごとに違う(`/lessons/external-license-differs`)。⑤読んでいない部分の内容を、題名や記憶で補わない。
- 「紹介されている」の意味: josh の資料のうち、読んだ範囲(ガイドブックの参照文献、2025 年度レポートの参照文献、OSC 2024 Kyoto と JSConf JP 2025 のスライド)に載っているもの。レポート本文の他の節、行政 OSS 調査の参照文献、読んでいない登壇資料に載っているものは確認できていない(`/open-questions/introduced-coverage`)。

# /assets/josh-reference-list
- status: verified
- source: guidebook-biases, report-2025, talk-osc-kyoto-2024, talk-jsconf-2025
- as_of: 2026-10-30
- 確認した事実(各資料の参照文献・引用として載っているもの。題名と発行主体のみ。本文は取り込まない):
  - ガイドブック(参照文献 2 件): InnerSource Commons の「InnerSource Principles」/ E. S. Raymond『The Cathedral and the Bazaar』(1999、書籍)。
  - OSC 2024 Kyoto(引用・参考): Open Source Guides「オープンソースプロジェクトを始めよう」/ Contributor Covenant「コントリビューター行動規範」/ GitHub Docs の CONTRIBUTING.md の例。
  - JSConf JP 2025(参考): Code for Development「Open-Source Policy Collection」/ 欧州委員会 FOSSEPS(Free and Open Source Software Solutions for European Public Services)。事例として、ドイツの Sovereign Tech Fund による Log4j への投資を挙げる。
  - 2025 年度レポート(参照文献 約 25 件。分類して列挙): 〔OSPO・貢献〕Linux Foundation「The 2025 State of OSPOs and Open Source Management」、同「ROI for Open Source Software Contribution」/〔資金・持続可能性〕Open Source Pledge、OpenForum Europe の EU-STF、Sovereign Tech Fund の事例研究(Interoperable Europe Portal)、Harvard Business School ワーキングペーパー「The Value of Open Source Software」/〔規制・政策〕欧州委員会の Cyber Resilience Act と「Cyber Resilience Act - Open source」、同「Open-Source Digital Ecosystems」の call for evidence、NIST の大統領令 14028 のページ、OpenForum Europe「Progress and trends in the national open source policies and legal frameworks」、欧州委員会の国別 OSS インテリジェンス報告(ポルトガル、ラトビア)/〔欧州の事例〕シュレスヴィヒ=ホルシュタイン州の発表 2 件、フランスの LaSuite/〔動向〕GitHub Octoverse 2025、Eclipse Foundation のブログ、The New Stack の記事、Open Source Initiative「Open Source AI」、Anthropic「Project Glasswing」/〔IPA 自身〕2024・2025 年度ソフトウェア動向調査、行政 OSS 国際比較調査報告書、LegalTech の推進。
- 注意: 上記のうち実際に取得して内容を確認したものは、`/sources/ext-*` のうち `introduced_by:` に josh の出典 id があるものだけ。ほかは題名・発行主体の確認にとどまる。

# /relationships/josh-and-external-literature
- status: verified, derived
- derives_from: /assets/josh-reference-list, /authorities/external-literature-handling
- source: guidebook-biases, report-2025, talk-osc-kyoto-2024, talk-jsconf-2025
- as_of: 2026-10-30
- 紹介されていて、取得して確かめたもの(`/sources/` に登録): InnerSource Commons の原則(ガイドブック)/ Open Source Guides の「始めよう」・Contributor Covenant(OSC 2024 Kyoto)/ Code for Development の政策集・FOSSEPS(JSConf JP 2025)/ LF の OSPO 調査 2025・LF の貢献 ROI・Open Source Pledge・CRA の OSS ページ(2025 年度レポート)。
- 紹介されていないもの(読んだ範囲に載っていない。`/sources/` に登録): TODO Group のガイド / CHAOSS の指標 / OpenSSF Scorecard / OpenSSF Best Practices バッジ / OpenChain / REUSE / Apache のプロジェクト成熟度モデル / CNCF TAG Contributor Strategy / Open Source Guides の別の 3 ページ(メンテナー向けベストプラクティス、リーダーシップと組織運営、メトリクス)/ 経産省の OSS 管理手法の事例集 / Sovereign Tech Agency。
- 注意: 「紹介されていない」は、読んだ範囲に載っていないという意味にとどまる。josh の未読部分が紹介している可能性は残る。Open Source Guides は「始めよう」が紹介されているサイトの別ページを含むので、サイト単位では「紹介されている」とも言える。

# /decision-support/practitioner-gains-from-josh
- status: derived
- derives_from: /assets/ospo-starter-kit, /assets/ospo-workbook, /assets/guidebook-biases, /assets/report-2025, /assets/report-govoss-2025, /assets/talks-library, /organization/hub-structure, /traces/ws-season1-held
- source: kit-page, kit-repo, workbook, guidebook-biases, report-2025, talk-osc-kyoto-2024, talk-jsconf-2025
- as_of: 2026-10-30
- 前提: 「すでに実践している人」を、組織で OSS の利用・管理に携わる担当者(A)と、OSS プロジェクトに貢献・運営する開発者やメンテナー(B)に分けて考えた。定義は作り手の仮置きで、確認が要る(`/open-questions/practitioner-definition`)。
- 解釈(A 組織の担当者が josh から得られること):
  1. 自社を測る物差し。2025 年度レポートの数値(OSS ポリシー整備率 36.7%、OSPO 設置率 4.1% など。調査年度・対象を添える。volatile)と、ガバナンスが整っていない企業が多いという IPA の認識は、自社の位置を相対化する材料になる。
  2. 既存の規程を点検するチェックリスト。スターターキット(CC0)の条文 0〜15 と運用テンプレートの構成を、自社の規程と突き合わせると、抜けや偏りが見つかる。ゼロから作る人向けの資料でも、実践者には「監査の視点」として使える。使い方文書の4つの柱(Mission / Incentive / Compliance / Engagement)も点検に使える。
  3. 社内を説得する言葉。ガイドブックの5つの処方箋と、役割別の要点メモ(経営・法務・財務・人事・組織開発)、ワークブックの第2〜4章(ステークホルダー、開発者、管理者へのメリットの言語化)。日本語で、CC BY で、出典を示せば引用できる。
  4. 同じ立場の実践の記録。OSPO レベル1構築ワークショップ(シーズン1)の記録と成果発表会は、他社の取り組み方の手がかりになる。ただし、現在参加募集中のイベントはない。
  5. 政策・規制の動向の把握。2025 年度レポートは、デジタル主権、EU サイバーレジリエンス法(CRA)、重要 OSS への公的支援を、日本の企業の視点で整理している。
- 解釈(B 貢献・運営する開発者やメンテナーが josh から得られること): 得られるものは A より少ない。①OSC 2024 Kyoto の資料が、コミュニティを持続可能にする基礎(ライセンス、README、コントリビュートガイドライン、行動規範を備える)を示す。②持続可能性と資金調達の動向(2025 年度レポート 4.3、JSConf JP 2025)が、支援を考える際の外部の情報になる。③ガイドブック処方箋4が、OSS 活動を雇用主に業務として認めてもらう論拠になりうる。
- 限界(josh が実践者に与えないもの): 読んだ範囲に、プロジェクト運営の具体的な手法(リリース管理、メンテナーの負担軽減、指標による健康度の測定)、セキュリティの実装(依存関係やビルドの強化、脆弱性対応の手順)、ライセンスコンプライアンスの運用ツールの解説はほとんどない。ハブの「OSSでつくる・育てる」は公開予定で、実践者に向く内容が入るかは不明(`/open-questions/coming-soon-menus`)。
- 注意: 以上は作り手の解釈で、IPA が実践者向けにそう述べているわけではない。

# /decision-support/literature-map-for-practitioners
- status: derived
- derives_from: /relationships/josh-and-external-literature, /decision-support/practitioner-gains-from-josh, /authorities/external-literature-handling
- source: ext-lf-state-of-ospos-2025, ext-lf-roi-contribution, ext-open-source-pledge, ext-innersource-commons, ext-osg-starting-a-project, ext-contributor-covenant, ext-c4d-oss-policies, ext-fosseps, ext-eu-cra-open-source, ext-todo-guides, ext-chaoss-metrics, ext-openssf-scorecard, ext-openssf-best-practices-badge, ext-openchain, ext-reuse, ext-asf-maturity-model, ext-cncf-tag-contributor-strategy, ext-osg-best-practices, ext-osg-leadership, ext-osg-metrics, ext-meti-oss-case-study, ext-sovereign-tech-agency
- as_of: 2026-10-30
- 注意: 選定は作り手(AI)の判断で、人の確認は未了。各項目の読んだ深さは `/sources/ext-*` の `ingest` と `notes` を見る。題名や要約が良さそうに見えることと、内容が良いことは別。
- 解釈(需要別の対応表。〔紹介〕は josh が紹介している、〔未紹介〕は読んだ範囲に載っていない):
  1. OSPO を運営・測定する: 〔紹介〕LF「2025 State of OSPOs」(OSPO の役割が準拠中心から戦略的ガバナンスに移りつつあるなどの調査。数値の根拠は未読)。〔未紹介〕TODO Group のガイド集(OSPO の作り方、戦略、成功の測り方、従業員の関与、採用などの題名のガイド。CC BY-SA 4.0)。josh のキットが「作る」側の雛形なのに対し、運用・測定側を補う。
  2. ライセンスコンプライアンスを回す: 〔未紹介〕OpenChain(ライセンス遵守の国際規格 ISO/IEC 5230 とセキュリティ保証の ISO/IEC 18974 を維持する LF の取り組み)、REUSE(ファイル単位でライセンスと著作権を機械可読に表示する FSFE の推奨)。josh のガイドブックは配布や SaaS の区別などの考え方を述べるが、運用の仕組みは扱わない。
  3. セキュリティとサプライチェーン: 〔紹介〕EU の CRA の OSS ページ(OSS に対する特別な扱いを説明するページ。条文の解釈は未確認)。〔未紹介〕OpenSSF Scorecard(OSS のリスクのある慣行を自動評価)、OpenSSF Best Practices バッジ(自己認証のベストプラクティス基準)。josh のガイドブックの3段階評価の実装手段になりうる。
  4. プロジェクトを運営する(B): 〔紹介〕Open Source Guides「始めよう」、Contributor Covenant。〔未紹介〕Open Source Guides の「メンテナーの為のベストプラクティス」「リーダーシップと組織運営」「メトリクス」、Apache のプロジェクト成熟度モデル(自己評価の枠組み)、CHAOSS の指標(コミュニティの健康度を測る。リポジトリは MIT)、CNCF の Contributor Strategy(メンテナーとの関係やガバナンスを扱う TAG。ただしリポジトリは 2025-11-03 にアーカイブ済み)。
  5. 社内で OSS の作法を練習する: 〔紹介〕InnerSource Commons の原則(ガイドブック処方箋5が参照)。
  6. 資金・持続可能性: 〔紹介〕Open Source Pledge(企業が開発者あたり年額を支払う約束)、LF「貢献の ROI」、FOSSEPS(欧州の公共機関の重要 OSS の調査)。〔未紹介〕Sovereign Tech Agency(josh は Sovereign Tech Fund の事例を引くが、同一組織かは未確認)。
  7. 政策の国際比較: 〔紹介〕Code for Development の政策集(ただし内容は CC BY-NC-ND 4.0 で、個別の政策文書は元のライセンス)。
  8. 日本の企業の実践事例: 〔未紹介〕経産省「OSSの利活用及びそのセキュリティ確保に向けた管理手法に関する事例集」(2021 年公開、2022 年 5 月に拡充。検索結果の記述では約 20 社の事例。経産省のサイトが自動取得を拒否したため、本文は未確認)。josh のキットとワークショップは日本企業の実務を扱うので、事例集は補完しうる。
- 読む順の目安(作り手の仮の提案): A は、josh のキットで自社の規程を点検 → TODO Group のガイドで運営・測定を補う → OpenChain/REUSE で運用の仕組みを調べる → 経産省の事例集(要確認)で他社と比べる。B は、josh の OSC 2024 資料 → Open Source Guides の3ページ → CHAOSS/Scorecard で自分のプロジェクトを測る。

# /scenarios/practitioner-using-josh
- status: derived
- derives_from: /decision-support/practitioner-gains-from-josh, /decision-support/literature-map-for-practitioners
- as_of: 2026-10-30
- 状況: すでに OSS を実践している人(組織の OSS 担当者、または貢献・運営している開発者)が、josh を自分の役に立てたい。
- 解釈: 入門や立ち上げの資料としてでなく、「自分の現状を点検する鏡」と「社内外を説得する根拠」として josh を使い、運営・測定・セキュリティの具体策は `/decision-support/literature-map-for-practitioners` の外部文献で補う。

# /lessons/external-license-differs
- status: derived
- derives_from: /authorities/external-literature-handling, /authorities/license-labels
- source: ext-c4d-oss-policies, ext-lf-state-of-ospos-2025, ext-todo-guides, ext-openchain, ext-reuse
- as_of: 2026-10-30
- 教訓: josh が勧める外部文献のライセンスは、josh の資料(主に CC BY / CC0)より厳しいものがありうる。Code for Development の政策集は CC BY-NC-ND 4.0、LF のレポートのページは「All rights reserved」の表示、TODO Group のガイドは CC BY-SA 4.0。引用や転載の前に、資料ごとに確かめる。

# /open-questions/practitioner-definition
- status: open
- as_of: 2026-10-30
- 問い: 「すでに OSS を実践している人」は誰を指すか。作り手は、組織の OSS 担当者(A)と、貢献・運営する開発者やメンテナー(B)に仮に分けたが、依頼者(hfu)の意図は確かめていない。個人の開発者か、OSPO を持つ企業か、行政かで、有用な文献の選び方が変わる。

# /open-questions/introduced-coverage
- status: open
- as_of: 2026-10-30
- 問い: josh が紹介している文献の全体像。読んだのは、ガイドブックの参照文献、2025 年度レポートの参照文献、2 つの登壇資料だけ。レポートの本文、行政 OSS 調査の参照文献、2024 年度レポート、未読の登壇資料に載る文献は確認していない。

# /open-questions/external-literature-depth
- status: open
- as_of: 2026-10-30
- 問い: `/sources/ext-*` の多くは、ページの冒頭や概要を読んだだけ(`ingest: 一部取り込み` か `未取り込み`)。各文献の中身が、実践者にとって実際にどの程度役に立つかは、まだ確かめていない。

# /open-questions/sovereign-tech-naming
- status: open
- as_of: 2026-10-30
- 問い: josh の資料が引く「Sovereign Tech Fund」と、現在のサイトの「Sovereign Tech Agency」は、同一の組織か、名称が変わったのか。サイトのトップページを読んだだけで、関係を述べた記述は確認していない。

# /open-questions/meti-case-study
- status: open
- as_of: 2026-10-30
- 問い: 経産省の OSS 管理手法の事例集の内容とライセンス。経産省のサイトが自動取得に 403 を返し、本文を取得できなかった。存在と概要は検索結果の記述(二次情報)による。

# /traces/cncf-tag-archived
- status: verified, volatile
- source: ext-cncf-tag-contributor-strategy
- as_of: 2026-10-30
- freshness: リポジトリの状態は変わりうる。使う前に確かめる。
- 事実: cncf/tag-contributor-strategy の GitHub リポジトリは、2025-11-03 にオーナーによってアーカイブ(読み取り専用)にされたと表示されている。内容の後継の所在は読んだ範囲に見当たらない。

# /sources/ext-innersource-commons
- status: verified
- title: InnerSource Principles(InnerSource Commons、学習パスの導入)
- issuer: InnerSource Commons Foundation
- published: 不明
- url: https://innersourcecommons.org/learn/learning-path/introduction/05/
- license: サイトは「別途表示がない限り CC-BY-SA」と表示
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- introduced_by: guidebook-biases
- notes: ページ冒頭(4 つの原則がある旨)のみ読んだ。ガイドブックが参照文献として挙げる。

# /sources/ext-osg-starting-a-project
- status: verified
- title: オープンソースプロジェクトを始めよう(Open Source Guides)
- issuer: Open Source Guides(GitHub が支援するガイド集)
- published: 不明
- url: https://opensource.guide/ja/starting-a-project/
- license: ページから確認できず
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- introduced_by: talk-osc-kyoto-2024
- notes: 立ち上げ前のチェックリスト(LICENSE、README・CONTRIBUTING・CODE_OF_CONDUCT などの基本文書、名前、イシューの整理)がある。全文は読んでいない。

# /sources/ext-contributor-covenant
- status: verified
- title: Contributor Covenant 行動規範 2.1(日本語)
- issuer: Contributor Covenant
- published: 不明(バージョン 2.1)
- url: https://www.contributor-covenant.org/ja/version/2/1/code_of_conduct/
- license: ページの本文から確認できず(OSC 2024 Kyoto の資料は、ほとんどが CC BY 4.0 と述べる)
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- introduced_by: talk-osc-kyoto-2024
- notes: 行動規範の雛形。違反時の対応段階(コミュニティへの影響ガイドライン)を含むことを確認した。

# /sources/ext-c4d-oss-policies
- status: verified
- title: Open Source Policy Documentation(Code for Development「Open-Source Policy Collection」)
- issuer: Code for Development(米州開発銀行のオープンソースイニシアチブとして JSConf JP 2025 の資料が紹介)
- published: 不明
- url: https://el-bid.github.io/OSS_policies/
- license: CC BY-NC-ND 4.0(リポジトリの内容。個々の政府の政策文書は元のライセンスを保持する、とページが述べる)
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- introduced_by: talk-jsconf-2025
- notes: 政策の種類別に整理した政策文書のサイト。JSConf JP 2025 は、この分類(9 類型)を引く。

# /sources/ext-fosseps
- status: verified
- title: FOSSEPS - Free and Open Source Software Solutions for European Public Services
- issuer: 欧州委員会 DIGIT(Interoperable Europe Portal)
- published: 不明
- url: https://interoperable-europe.ec.europa.eu/collection/fosseps
- license: 確認していない
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- introduced_by: talk-jsconf-2025
- notes: 欧州の公共機関の OSS を集合的な資産として管理・保護する必要を述べる紹介ページ。調査の中身(JSConf JP 2025 が述べる、重要 OSS の特定とバスファクターの課題)の一次資料は未読。

# /sources/ext-lf-state-of-ospos-2025
- status: verified
- title: The 2025 State of OSPOs and Open Source Management
- issuer: LF Research(The Linux Foundation)
- published: 不明(ページに日付の表示なし)
- url: https://www.linuxfoundation.org/research/ospo-2025
- license: ページに利用許諾の表示なし。フッターは All rights reserved の著作権表示
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- introduced_by: report-2025
- notes: ページの概要を読んだ(要約ツール経由)。OSPO が準拠中心から戦略的ガバナンスに移りつつあること、OSPO を持つ組織で上流貢献が多いことなどの調査結果が述べられている。調査の方法・標本は、ページには見当たらず、PDF は未取得。

# /sources/ext-lf-roi-contribution
- status: verified
- title: ROI for Open Source Software Contribution
- issuer: LF Research(The Linux Foundation)
- published: 不明(2025 年度レポートは 2026-02 の公表として引く)
- url: https://www.linuxfoundation.org/research/contribution-roi
- license: 確認していない
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 未取り込み
- introduced_by: report-2025
- notes: ページの存在(HTTP 200)とタイトルを確認しただけ。本文は読んでいない。

# /sources/ext-open-source-pledge
- status: verified
- title: Open Source Pledge
- issuer: Open Source Pledge
- published: 不明
- url: https://opensourcepledge.com/
- license: 確認していない
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- introduced_by: report-2025
- notes: トップページを読んだ。企業がメンテナーに直接現金を拠出する取り組みで、累計の拠出額が表示されている(2026-10-30 時点で約 920 万ドルとの表示。2025 年度レポートの「約 700 万ドル超(2026 年初時点)」と時点が違う。volatile)。

# /sources/ext-eu-cra-open-source
- status: verified
- title: Cyber Resilience Act - Open source
- issuer: 欧州委員会(Shaping Europe's digital future)
- published: 不明(2025 年度レポートは 2026-01-12 付として引く)
- url: https://digital-strategy.ec.europa.eu/en/policies/cra-open-source
- license: 確認していない
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- introduced_by: report-2025
- notes: 冒頭(CRA は FOSS に対して特別な扱いをとる、とする説明)のみ読んだ。法的な解釈は行わない。

# /sources/ext-todo-guides
- status: verified
- title: Guides and Resources(TODO Group の OSPO ガイド集)
- issuer: TODO Group(The Linux Foundation 傘下のコミュニティ)
- published: 不明
- url: https://todogroup.org/resources/guides/
- license: OSPO ガイドは CC BY-SA 4.0、ページのフッターは別途表示がない限り CC BY 4.0(ページの表示を要約ツール経由で確認)
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- introduced_by: なし(読んだ範囲では)
- notes: ガイド一覧のページを読んだ。OSPO の FAQ、作り方、戦略、成功の測り方、コード利用、公開(アウトバウンド)、ツール、従業員の関与、キャリア、採用などの題名がある。各ガイドの本文は未読。

# /sources/ext-chaoss-metrics
- status: verified
- title: CHAOSS Metrics(GitHub リポジトリ)
- issuer: CHAOSS Project(The Linux Foundation 傘下)
- published: 不明
- url: https://github.com/chaoss/metrics
- license: MIT(リポジトリの LICENSE を確認)
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- introduced_by: なし(読んだ範囲では)
- notes: README を読んだ。コミュニティの健康度の指標を、ワーキンググループ(共通、多様性と包摂、進化、価値、リスク)が作る。現行版は chaoss.community/metrics にあるとされるが、そのサイトは自動取得に 403 を返したため確認できていない。

# /sources/ext-openssf-scorecard
- status: verified
- title: OpenSSF Scorecard
- issuer: Open Source Security Foundation
- published: 不明
- url: https://scorecard.dev/
- license: 確認していない
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- introduced_by: なし(読んだ範囲では)
- notes: トップページを読んだ。OSS のリスクのある慣行を評価する仕組みで、GitHub Action で自動実行するか、コマンドラインで他者のプロジェクトを手動評価できると説明している。個々の検査項目は未読。

# /sources/ext-openssf-best-practices-badge
- status: verified
- title: OpenSSF Best Practices Badge Program
- issuer: Open Source Security Foundation
- published: 不明
- url: https://www.bestpractices.dev/en
- license: ページ内に CC-BY-3.0 の表示があるが、何に対するものかは確認していない
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- introduced_by: なし(読んだ範囲では)
- notes: プロジェクトが無償で自己認証し、ベストプラクティスに従っていることを示すバッジ制度と説明している。基準の本文は未読。

# /sources/ext-openchain
- status: verified
- title: OpenChain
- issuer: OpenChain Project(The Linux Foundation)
- published: 不明
- url: https://openchainproject.org/
- license: 仕様は CC-BY-4.0、参考資料は CC0(サイトフッターの表示)
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- introduced_by: なし(読んだ範囲では)
- notes: トップページを読んだ。OSS のライセンス遵守の規格 ISO/IEC 5230 とセキュリティ保証の規格 ISO/IEC 18974 を維持する取り組みと説明している(要約ツール経由)。規格の本文は未読。

# /sources/ext-reuse
- status: verified
- title: REUSE - Make licensing easy for everyone
- issuer: Free Software Foundation Europe(REUSE SOFTWARE)
- published: 不明
- url: https://reuse.software/
- license: サイトは別途表示がない限り CC BY-SA 4.0
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- introduced_by: なし(読んだ範囲では)
- notes: ライセンスの選択と提供、ファイルごとの著作権・ライセンス情報の付与、準拠の確認、という3段階の推奨を述べる。仕様の本文は未読。

# /sources/ext-asf-maturity-model
- status: verified
- title: A Maturity Model for Apache Projects
- issuer: The Apache Software Foundation(Community Development)
- published: 不明
- url: https://community.apache.org/apache-way/apache-project-maturity-model.html
- license: 確認していない
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- introduced_by: なし(読んだ範囲では)
- notes: プロジェクトのコミュニティとコードベースの成熟度を評価する枠組みの提案。ASF 固有だが多くの要素は他のプロジェクトにも当てはまる、と冒頭が述べる。評価項目の本文は未読。

# /sources/ext-cncf-tag-contributor-strategy
- status: verified
- title: CNCF Technical Advisory Group on Contributor Strategy(GitHub リポジトリ)
- issuer: CNCF
- published: 不明
- url: https://github.com/cncf/tag-contributor-strategy
- license: リポジトリにライセンス表示があるが(Apache-2.0 とみられる)、対象は確認していない
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- introduced_by: なし(読んだ範囲では)
- notes: メンテナーとの関係、コントリビューターの育成、ガバナンスなどを扱う TAG と説明している。2025-11-03 にアーカイブされた(`/traces/cncf-tag-archived`)。内容は未読。

# /sources/ext-osg-best-practices
- status: verified
- title: メンテナーの為のベストプラクティス(Open Source Guides)
- issuer: Open Source Guides
- published: 不明
- url: https://opensource.guide/ja/best-practices/
- license: ページから確認できず
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- introduced_by: なし(読んだ範囲では。同サイトの別ページ「始めよう」は紹介されている)
- notes: 冒頭を読んだ。プロセスのドキュメント化、コミュニティの活用など、メンテナーの負担を軽くする方法を述べる。

# /sources/ext-osg-leadership
- status: verified
- title: リーダーシップと組織運営(Open Source Guides)
- issuer: Open Source Guides
- published: 不明
- url: https://opensource.guide/ja/leadership-and-governance/
- license: ページから確認できず
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- introduced_by: なし(読んだ範囲では。同サイトの別ページ「始めよう」は紹介されている)
- notes: 冒頭を読んだ。成長するプロジェクトの運営、役割(メンテナー、コントリビューター、コミッター)、コミット権限の与え方などを扱う。

# /sources/ext-osg-metrics
- status: verified
- title: メトリクス(Open Source Guides)
- issuer: Open Source Guides
- published: 不明
- url: https://opensource.guide/ja/metrics/
- license: ページから確認できず
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 一部取り込み
- introduced_by: なし(読んだ範囲では。同サイトの別ページ「始めよう」は紹介されている)
- notes: 冒頭を読んだ。データに基づく意思決定、利用状況の把握、スポンサーや補助金の獲得に計測を使う、といった点を述べる。

# /sources/ext-meti-oss-case-study
- status: verified
- title: OSSの利活用及びそのセキュリティ確保に向けた管理手法に関する事例集
- issuer: 経済産業省
- published: 2021-04-21 公開、2022-05-10 拡充(検索結果の記述による。二次情報)
- url: https://www.meti.go.jp/policy/netsecurity/wg1/ossjirei_20220510.pdf
- license: 確認できず
- license_checked_at: 2026-10-30
- fetched_at: 未取得(自動取得が 403 を返した)
- ingest: 未取り込み
- introduced_by: なし(読んだ範囲では)
- notes: 存在と概要は、検索結果の記述(約 20 社の事例、PDF 約 135 ページ、ソフトウェア管理手法等検討タスクフォースの議論が出発点)による。本文は確認していない。URL は検索結果が示したもので、直接開いて確かめていない。→ `/open-questions/meti-case-study`

# /sources/ext-sovereign-tech-agency
- status: verified
- title: Sovereign Tech Agency
- issuer: Sovereign Tech Agency
- published: 不明
- url: https://www.sovereign.tech/
- license: 確認していない
- license_checked_at: 2026-10-30
- fetched_at: 2026-10-30
- ingest: 未取り込み
- introduced_by: 不明(josh は「Sovereign Tech Fund」を引く。同一組織かは未確認)
- notes: トップページのタイトルと標語(21 世紀のインフラへの投資)のみ。→ `/open-questions/sovereign-tech-naming`

# /acceptance-tests/practitioner-gains-from-josh
- query: OSS をすでに実践している人にとって、josh から得られることは何か。
- scope: 範囲内
- expected: 「実践者」の仮定(組織の担当者と、貢献・運営する開発者)を示したうえで、組織の担当者には、自社を測る物差し(2025 年度レポートの数値、volatile)、既存規程の点検用チェックリスト(キット)、社内説得の言葉(ガイドブック、ワークブック)、他社の実践の記録(ワークショップ)、政策・規制の動向を挙げる。開発者・メンテナーには得られるものが少ないこと(OSC 2024 の基礎、資金の動向、業務化の論拠)と、josh が与えないもの(運営手法、セキュリティの実装、コンプライアンス運用)を述べる。作り手の解釈で、IPA の述べたことではないと区別する。
- requires: /decision-support/practitioner-gains-from-josh, /scenarios/practitioner-using-josh, /open-questions/practitioner-definition
- result: pass
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: キットの各条文・ワークブック演習の本文(点検用としての具体的な使い方の裏づけ)。
- missing_source_limit: 実践者を読者とした josh の記述は出典にない(ハブは読者像を定義していない)。
- freshness: 数値は年次で更新される。「OSSでつくる・育てる」の公開で変わりうる。

# /acceptance-tests/practitioner-other-references
- query: OSS をすでに実践している人は、josh 以外の何を参考にするべきか。josh が紹介している文献と、紹介していない文献の両方から示してほしい。
- scope: 範囲内
- expected: 紹介されている文献と紹介されていない文献を区別して示す(読んだ範囲の限定つき)。紹介されている例: LF の OSPO 調査 2025、InnerSource Commons、Open Source Guides「始めよう」、Contributor Covenant、Code for Development、FOSSEPS、Open Source Pledge、CRA の OSS ページ。紹介されていない例: TODO Group のガイド、OpenChain、REUSE、OpenSSF Scorecard・Best Practices バッジ、CHAOSS、Apache の成熟度モデル、Open Source Guides の別ページ、経産省の事例集(未確認と明示)。需要別(OSPO の運営、コンプライアンス、セキュリティ、プロジェクト運営、資金、日本の事例)に対応づける。選定が作り手の判断で、IPA の推薦ではなく、人の確認が未了であることを添える。
- requires: /decision-support/literature-map-for-practitioners, /relationships/josh-and-external-literature, /assets/josh-reference-list, /authorities/external-literature-handling
- result: partial
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: 各外部文献の本文(多くはページの冒頭のみ)、経産省の事例集の本文、josh の未読部分に載る文献。
- missing_source_limit: 外部文献の質や実践者への有用性を比較した出典はない。選定は作り手の判断にとどまる。
- freshness: 外部サイトの状態は変わる(例: CNCF TAG のアーカイブ)。Open Source Pledge の累計額などは volatile。

# /acceptance-tests/reuse-license-of-recommended-literature
- query: josh が紹介している・勧めている外部文献のうち、自社の研修資料に転載しやすいのはどれか。
- scope: 範囲内
- expected: 文献ごとにライセンスが違うので一括では答えられない。確認できたものとして、OpenChain の仕様は CC-BY-4.0、参考資料は CC0、TODO Group のガイドは CC BY-SA 4.0、REUSE と InnerSource Commons のサイトは CC BY-SA 系、CHAOSS の指標のリポジトリは MIT、Code for Development の内容は CC BY-NC-ND 4.0(転載・改変に不向き)、LF の OSPO 調査のページは All rights reserved の表示。ライセンスを確認できなかったもの(Open Source Guides、Scorecard、ASF、CNCF、経産省)は未確認と答える。法的判断ではない。
- requires: /lessons/external-license-differs, /authorities/external-literature-handling, /procedures/reuse-hub-material
- result: partial
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: ライセンスを確認できなかった文献のライセンス表示(ページ外の利用条件の確認を含む)。
- missing_source_limit: 個別の利用が条件を満たすかの法的判断は出典にない。
- freshness: ライセンス表示は変わりうる。利用の直前に確かめる。

# /acceptance-tests/is-scorecard-introduced-by-josh
- query: OpenSSF Scorecard は、josh が紹介している文献か。
- scope: 範囲内
- expected: 読んだ範囲(ガイドブックと 2025 年度レポートの参照文献、2 つの登壇資料)には載っていない。ただし josh の未読部分(レポート本文、他の資料)に載っている可能性は残るので、「紹介されていない」と断定せず、「読んだ範囲に見当たらない」と答える。
- requires: /relationships/josh-and-external-literature, /open-questions/introduced-coverage
- result: pass
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: 2025 年度レポート本文の全節、未読の登壇資料。
- missing_source_limit: 「ある文献が載っていない」ことを、出典の全部を読まずに証明することはできない。
- freshness: josh の資料が更新されると変わる。

# /acceptance-tests/maintainer-starting-reading-list
- query: OSS プロジェクトを運営しているメンテナーが、まず読むべきものは何か。
- scope: 範囲内
- expected: josh では OSC 2024 Kyoto の資料(基本文書と行動規範の整備)が出発点。josh の外では、Open Source Guides の「メンテナーの為のベストプラクティス」「リーダーシップと組織運営」「メトリクス」、Contributor Covenant(josh が紹介)、CHAOSS・Apache の成熟度モデル・OpenSSF のバッジや Scorecard を、自己点検に使える候補として示す。josh の資料はメンテナー向けに書かれていないこと、CNCF の Contributor Strategy がアーカイブ済みであることも添える。
- requires: /decision-support/literature-map-for-practitioners, /scenarios/community-operator-reading
- result: partial
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: 各ガイドの本文、CHAOSS の指標の現行版(サイトが自動取得を拒否)。
- missing_source_limit: メンテナーに「まず読むべき」順序を決めた出典はない。順序は作り手の仮の提案。
- freshness: 外部サイトの状態は変わる。

# /acceptance-tests/japan-company-practice-cases
- query: 日本の企業の OSS 管理の実践事例は、どこで読めるか。
- scope: 範囲内
- expected: josh では、OSPO レベル1構築ワークショップの記録と成果発表会の資料(ゲスト講師は企業の OSPO 担当者だが、個人名は kcaim に書かない)。josh の外では、経産省の事例集(2021 年公開、2022 年拡充、約 20 社とされる)があるが、本文は取得できておらず、内容は未確認と明示する。
- requires: /traces/ws-season1-held, /sources/ext-meti-oss-case-study, /open-questions/meti-case-study
- result: partial
- result_by: 作成者の自己実行。kcaim 全体と取得済みメモを参照
- missing_ingest: 経産省の事例集の本文、ワークショップ・成果発表会の PDF。
- missing_source_limit: 事例の網羅性を述べた出典はない。
- freshness: 事例集は更新されうる。

# /inventory/ingest-and-backlog
- status: derived
- derives_from: /sources/hub-library, /acceptance-tests/implications-for-developers, /acceptance-tests/implications-for-community-operators
- as_of: 2026-10-30
- 出典ごとの取り込み状況:
  - 取り込み済み: hub-top, hub-about, hub-learn, hub-events, hub-report, hub-adopt, hub-library, kit-page, ws-season1-archive, talk-jsconf-2025, talk-osc-kyoto-2024
  - 一部取り込み: kit-repo(条文 0〜15 と多くの運用テンプレートが未読), workbook(PDF 演習本文が未読), guidebook-biases, report-2025(第2章以降が未読), report-govoss-2025(本文が未読), series-economic-value(目次のみ)
  - 未取り込み: talk-foss4g-2025-kansai(CC BY-SA のため意図的に未取得)
  - 外部文献(`/sources/ext-*`、22 件。josh が紹介しているもの 9 件、読んだ範囲で紹介されていないもの 12 件、不明 1 件): 一部取り込み 19 件(ページの冒頭・概要のみ)、未取り込み 3 件(LF の貢献 ROI、経産省の事例集、Sovereign Tech Agency)。本文を読み込んだものはない。
  - 概要のみ(出典として未登録): 2024 年度レポート、「思い込み」アンケートのまとめ、行動規範ページ、コラム 2 本、ほか登壇資料 12 件、ワークショップ配布資料 5 点
- 受け入れテストのバックログ(追加したい問い): AI 時代の OSS ガバナンス(2025 年度レポート第4章)/ EU サイバーレジリエンス法への対応(同レポート提言5)/ インナーソースとは何か(ガイドブック処方箋5・キット)/ ワークショップ第2回・第3回の内容と学び / 日本型 OSS モデルの 3 軸とは / OSS ポリシーの条文の構成 / ハブの更新を追う方法。
- エージェントが自律的に進められる次の行動:
  1. ガイドブックの処方箋2〜5とあとがきの本文を要約して取り込む(`/assets/guidebook-biases` を更新)。
  2. 2025 年度レポートの第4章(特に 4.3)と第7章を要約して取り込む。
  3. コラム 2 本と連載 4 回を取得し、ライセンス表記を `/open-questions/column-license` に反映する。
  4. キットの条文 0〜15 と運用テンプレートを読み、`/assets/ospo-starter-kit` に条文ごとの論点を足す。
  5. 受け入れテストを追加し、再実行する。
- 人に引き継ぐ項目:
  1. 内容の確認(人による確認は未了)。特に `derived` と、「読んだ範囲に見当たらない」と書いた否定の事実。
  2. 盲検の実行(別の主体が、この kcaim だけを持って受け入れテストに答える)。
  3. 組織改編の対応関係(`/open-questions/org-mapping`)など、ハブの外の確認や IPA への問い合わせが要る事項。
  4. GitHub への公開の判断と手順(未実施)。
- `volatile` なオブジェクト: /traces/cncf-tag-archived, /sources/ext-open-source-pledge(累計額), /assets/ospo-starter-kit, /assets/report-2025, /assets/report-govoss-2025, /organization/ipa-units, /organization/hub-structure, /relationships/inquiry-channel, /traces/org-reform-2026-08-01, /open-questions/coming-soon-menus, /open-questions/kit-releases
- 定期の確認: ハブのトップ(お知らせ)とライブラリの更新履歴を、少なくとも月 1 回確かめる。

# /system-record/self-run-log
- 実施日: 2026-10-30。実施者: この kcaim を書いた AI(同一主体)。記憶を使わず、kcaim の内容と取得済みメモだけで各テストに答える方式で `result` を決めた。結果を良く見せるための書き換えはしていない。
- 1 回目(17 件): pass 8 / partial 5 / fail 1 / volatile 3。partial は implications-for-developers, implications-for-community-operators, government-oss-vs-other-countries, reuse-in-training-material, community-sustainability-points。
- 追記(1 回だけ): 取得済みのファイルで安価に埋められる不足として、ガイドブック処方箋2〜5の本文、2025 年度レポート 4.3、連載・コラムのライセンス表記の有無を取り込んだ。
- 2 回目(17 件): pass 10 / partial 3 / fail 1 / volatile 3。変わったのは 2 件で、どちらも partial → pass: implications-for-developers, community-sustainability-points。ほかの partial(community-operators, government-oss, reuse-in-training)は、取り込みを増やしても、残る不足(コラム本文、国別の分析章、イベント資料のライセンス)が埋まらないので変えていない。
- 2 回目で見つかった誤り: 1 回目の `expected` と `/scenarios/developer-first-contribution` に、「ハブに開発者個人向けの手引きは少ない・見当たらない」という書き方があった。ガイドブックが対象者に開発者を明記し、ワークブックに開発者向けの章があるため、「開発者を読者に含めている」が正しい。事実の記述を直し、`expected` を修正した(結果の書き換えではなく、問いの期待の誤りの訂正)。
- 偏りの可能性: 出題と採点が同じ主体なので、`pass` は楽観側に偏りうる。`pass` の多くは「この kcaim に書いたことを答えられる」ことの確認で、「この kcaim が重要な問いを網羅している」ことの確認ではない。盲検の実行(別の主体)が必要。範囲外のテスト 2 件は、境界を示す側の期待が自分で書きやすいので、特に偏りやすい。
- 検査器の WARN: 初回に 18 件。すべて `/sources/*` が `verified` で `source:` を持たないことによるもので、出典オブジェクトは自分が出典なので、検査器側を直した(`/sources/` は対象外)。最終は WARN 0 件。

# /system-record/format-observations
- status: derived
- derives_from: /system-record/self-run-log
- as_of: 2026-10-30
- 内容: この作業で気づいたこと(kcaim の FORMAT.md に返すためのメモ)。実際に作業して気づいたことだけを書いた。
  1. front matter の必須キー: 仕様の例は 10 個のキー(`kcaim_format` を含む)を示すが、本文は「9つ」と数えていた。検査器は 10 個を必須にした。数え方を FORMAT 側で一意にしたい。
  2. front matter と `/system-record/instance` の重複: `title`・`as_of`・`scope`・`disclaimer` が front matter と system-record の両方に現れ、食い違いうる。kcaim の例(`kcaim-bird-yezo.md`)は front matter を持たず、system-record に情報を置いている。単一ファイルの原則と front matter の整合は未確認(D-009)。重複を許すか、front matter を索引用の最小限にするか、決めたい。
  3. 状態の語彙の過不足: (a) 否定の事実が足りない。「読んだ範囲のページに、この記述が見当たらない」という事実(ハブが読者像を定義していない、運営者を直接扱っていない)は、`verified`(ある記述を確かめた)とも `open`(未解決)とも言い切れない。「未発見(範囲つき)」のような状態が要る。(b) 1 つのオブジェクトに事実と主張が混ざるので、オブジェクト単位の `status: verified, stated` では区別できず、実際には行頭の「確認した事実:」「述べられていること:」「解釈:」という書き分けが役割を担った。状態はオブジェクトでなくフィールド(行)単位にする案がある。(c) `ingest` は内容の状態と別の語彙にして正解だった。
  4. 仮想パスの足りなさ・余り: 足りなかった種別は、読者・主体の区分(`/organization` に入れた)、ハブ自身の目的の記述(同)。余った種別は `/operations`、`/reference-concepts`(使わなかった)。`/relationships` は連絡の機能と IPA の立ち位置に使えた。`/inventory` は 1 件にまとまったが、取り込み状況の表としては機械可読にしたい。
  5. 参照の検査: `source:` の参照先は検査器で確かめられるが、`derives_from:` と `requires:` が指すパスの存在は検査していない(作業の最後に別のスクリプトで確かめた)。検査の対象にする価値がある。
  6. `/sources/` 自身の扱い: 出典オブジェクトに `verified` を付けると `source:` なしの WARN になる。出典の書誌が確認済みであることの表し方を決めたい。
  7. ファイルの大きさ: 出典 18 件・受け入れテスト 17 件・約 95 オブジェクトで、約 87 KB・約 4.6 万字になった。出典と受け入れテストで約 4 割を占める。1 つのエージェントが常に携行する大きさとして許容かは、盲検の結果を見て判断したい。分割の目安(上限)が要る。
  8. 取り込みの衛生: PDF のテキスト抽出で一部の語に字形の置換が起きた(例:「権利」が別の字に化ける)。数値や固有名詞を写すときの確認が要る。また、CC BY の資料を要約する場合の出典表示は `/sources/` の `notes` に書く運用にした。
  9. 個人名: 資料の書誌には執筆者・登壇者の個人名がある。この kcaim は最小限どころか省略した(所属・機能で記した)。FORMAT で、個人名の扱いの基準を決めたい。
  10. 日付の食い違い: ハブの複数ページで、同じ出来事(組織改編に伴う問い合わせ先の更新)の日付が一致しない。出典間の食い違いを `/traces` と `/open-questions` に分けて記録する書き方は機能した。

