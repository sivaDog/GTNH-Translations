# GregTech 単独名(non-material)メタアイテムの翻訳欠落調査

調査日: 2026-08-17
きっかけ: 「Thick Cardboard (#7495/21879)」の翻訳先を探したところ見つからなかった件

## 結論(先に)

- `gt.metaitem.01.21879.name=Thick Cardboard` (旧レガシーcfg形式 `.minecraft/GregTech.lang` / `daily-history/GregTech.lang`) は
  **もう使われていない凍結データ**。現行の翻訳先ではない。
- 現行の翻訳先は `config/txloader/load/GregTech[gregtech]/lang/ja_JP.lang` の `gt.oreprefix.thick_cardboard`。
  **こちらは既に「厚いボール紙」に翻訳済み**（リポジトリ・ローカルインスタンス両方で確認済み）。
- 同様の懸念で457件(旧metaitem形式で単独名だったもの)を全数チェックした結果、
  - 396件: 新形式ファイルに移行済み・翻訳済み
  - 3件: 新形式ファイルに移行済みだが未翻訳(下記)
  - **49件: 現行パイプラインのどこにも存在しない、本当の欠落**(下記)
- 「Inflection Managerに追加登録すれば直せるか」という問いへの回答: **NO**。
  Inflection Managerは `%s{key}` プレースホルダを含む「OrePrefix×Material」テンプレート文字列専用の
  文法変化(語形変化)解決機構であり、プレースホルダを持たない固定名アイテムは対象外。
  Cardboard系も含め、いずれも `gt.oreprefix.xxx=固定文字列` という形で登録されており、
  Inflection Managerの処理対象にすら入らない。49件の対応を求めるIssueは
  「Inflection Managerへの追加」ではなく「PR #6064と同様の`en_US.lang`移行」を依頼する内容にすべき。

## 経緯・調査の流れ

1. `.minecraft/GregTech.lang` (line 47509) に `S:gt.metaitem.01.21879.name=Thick Cardboard` を発見。
   `.minecraft/GregTech_ja_JP.lang` (line 49504) も同じ英語のまま(未翻訳に見えた)。
2. GTNH-Translationsリポジトリの同期元 `daily-history/GregTech.lang` には該当キー含め
   `gt.metaitem.01.<数字>.name=` 形式の行が **1件も存在しない**(ローカルは6738件)。
3. git履歴を遡ると、2026-05-06のコミット `a2dc18900` (PR #63 "update GregTech.lang", by Quetz4l)で
   65,959行を削除(2,164行のみ残す)。PR説明: "new system for template names"、
   [Inflection Manager](https://wiki.gtnewhorizons.com/wiki/Inflection_Manager) へのリンクあり。
4. GT5-Unofficial側の実装元PRを特定:
   - [#6229 "add Inflection Manager to help translation"](https://github.com/GTNewHorizons/GT5-Unofficial/pull/6229) (merged 2026-05-01)
     → `OrePrefixes`/`Materials`/`Werkstoff`(Bartworks)/Fluid関連のみ変更。MetaGeneratedItemの標準名は対象外。
   - [#6064 "Add localization support for MetaGeneratedItem display names and tooltips"](https://github.com/GTNewHorizons/GT5-Unofficial/pull/6064) (merged 2026-03-26)
     → GT Credit/Coin/Electric Motor/Electric Piston/Solar Panel(高Tier)等、多数のMetaGeneratedItemカテゴリを
     初期化時凍結方式から `en_US.lang` ベースの実行時解決方式へ移行。Cardboard系はこのPRの一覧には
     明記されていないが、実際には `gt.oreprefix.*` キーとして同様に移行済みだった。
5. 実際に `daily-history/resources/GregTech[gregtech]/lang/en_US.lang` を確認したところ、
   Cardboard/Carton/Paperboard/Thick Cardboard は `gt.oreprefix.cardboard` 等のキーで存在し、
   対応する `ja_JP/config/txloader/load/GregTech[gregtech]/lang/ja_JP.lang` に既に日本語訳あり。
   → 当初「449件が完全に消失」と判断したが、これは誤りで、大半は既に正しい場所へ移行済みだった。

## 検証方法

ローカル実インスタンス `.minecraft/GregTech.lang` の `gt.metaitem.01.<ID>.name=` 全6738件から、
`%material` 等のプレースホルダを含まない(=テンプレート化されていない)単独名 449件を抽出。
これを `daily-history/resources/*/lang/en_US.lang` 全体(値の完全一致)で照合し、
見つかったものは対応する `ja_JP/.../lang/ja_JP.lang` の翻訳状況も確認した。

## 未翻訳3件(移行先は存在、翻訳するだけでよい) — **2026-09-22 に対応済み**

| キー | 英語 | 投入した訳 | 根拠 |
|---|---|---|---|
| `gt.item.paper.magic.page.name` | Enchanted Page | `エンチャントされたページ` | 系列の `gt.item.paper.magic.empty.name=魔法の紙` に合わせた。zh_CN `附魔书页` / ko_KR も単複同一表記 |
| `gt.item.paper.magic.pages.name` | Enchanted Pages | `エンチャントされたページ` | 日本語は複数を表記しない。兄弟の `Printed Pages=印刷されたページ` も同様 |
| `tile.solar.name` | Solar Panel | `ソーラーパネル` | 同ファイルの `tile.dummyblock.solar.name` / `item.basicItem.solar_module_1.name` と同表記。他 Mod との衝突なし |

以下は当時の記録:


| ID | 英語名 | キー | ファイル |
|---|---|---|---|
| 32483 | Enchanted Page | `gt.item.paper.magic.page.name` | `GregTech[gregtech]/lang/ja_JP.lang` |
| 32484 | Enchanted Pages | `gt.item.paper.magic.pages.name` | `GregTech[gregtech]/lang/ja_JP.lang` |
| 32750 | Solar Panel | `tile.solar.name` | `Galacticraft Core[galacticraftcore]/lang/ja_JP.lang` |

## 真の欠落49件(現行パイプラインのどこにも存在しない)

Wireless Energy Cover (LV〜MAXの全14Tier、ID 32383-32396)、Large Chrome Fluid Cell (32410)、
Spray Can 各色×2 (32430-32461、黒/赤/緑/茶/青/紫/シアン/ライトグレー/グレー/ピンク/ライム/黄/ライトブルー/マゼンタ/オレンジ/白)、
Redstone Transmitter (External, 32741)、Redstone Receiver (External/Internal, 32746-32747)。

全リストは同ディレクトリに保存:
`gregtech-standalone-449-candidates.tsv` (元449件の候補), `gregtech-standalone-49-truly-missing.tsv` (真の欠落49件)。

## Issueを立てる場合の方針

- 宛先: GTNH-Translationsではなく **GT5-Unofficial** (MetaGeneratedItemの名前がそもそも
  lang化されていないのが根本原因のため)。
- 内容: 「PR #6064で移行された他のMetaGeneratedItemカテゴリと同様に、以下49件のTile Cover/Spray Can/
  Wireless Energy Cover系アイテムも `en_US.lang` ベースのローカライズに移行してほしい」という主旨。
- 「Inflection Managerに追加してほしい」という表現は不適切(対象範囲が違うため)。
  あくまで「PR #6064方式のlang移行がまだされていない項目」という説明にする。


## 【訂正】「真の欠落49件」は 2026-09-22 時点で全件解消していた

この調査(2026-08-17)の「49件は現行パイプラインのどこにも存在しない」という結論は**誤り**だった。
正しくは **49件すべて現行 `en_US.lang` に存在し、日本語訳も入っている**。
`notes/gregtech-standalone-49-truly-missing.csv` は削除した(バックアップ: `scratchpad/tsv-backup-20260922/`)。
アップストリームに issue を立てる必要は無い。

| 件数 | 旧 metaitem 名 | 現行キー | 日本語 |
|---:|---|---|---|
| 32 | `Spray Can (<16色>)` ×2 | `gt.item.spray_can.dye.name=Spray Can (%s)` | `染料入りスプレー缶 (%s)` |
| 14 | `<tier> Wireless Energy Cover` | `gt.item.wireless_energy_cover.name=%s Wireless Energy Cover` | `無線エネルギーカバー (%s)` |
| 1 | `Large Chrome Fluid Cell` | `gt.item.large_fluid_cell.chrome.name`(英名も `Large Rhodium-Plated Palladium Fluid Cell` に変更) | `ロジウムメッキパラジウム製大型流体セル` |
| 1 | `Redstone Transmitter (External)` | `gt.item.cover.redstone_transmitter.name`(External 版が既定になり `(Internal)` だけが別キーに) | `レッドストーン送信機` |
| 1 | `Redstone Receiver (External)` | `gt.item.cover.redstone_receiver.name` | `レッドストーン受信器` |

### 誤判定の原因

照合を**英文の完全一致**で行っていたため。Tier や色が `%s` に畳まれたテンプレートキーへ移行すると、
`LV Wireless Energy Cover` は `%s Wireless Energy Cover` と一致せず「消滅」と判定されてしまう。
`gt.item.large_fluid_cell.chrome` のように英名そのものが変わった例もある。

**同種の照合をするときは、Tier 語・数字・色名を伏字にしてから比較すること。**
(`ja-key-change-audit-2026-09-22.md` の `GONE_family_removed` 再検証でも同じ罠を踏んでいる)
