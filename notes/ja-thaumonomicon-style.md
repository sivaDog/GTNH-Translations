# 日本語ソーモノミコン翻訳スタイルメモ（sivaDog）

ParaTranz / 手元ドラフト共通。クエストブック（`notes/ja-quest-style.md`）とは **口調も書式も別**。既存の良い訳（本体 Thaumcraft と dreamcraft の TinyUranium・満たされた壺・栄養のタリスマン）に揃える。

対象の主ファイル:

- GTNH 追加研究: `ja_JP/config/txloader/load/GT_ New Horizons[dreamcraft]/lang/ja_JP.lang`
- 本体 TC の用語・口調の規範: `ja_JP/config/txloader/load/Thaumcraft[thaumcraft]/lang/ja_JP.lang`

## 口調（最重要）

- 本文は **常体（だ・である・した・だろう）**
- **独白／研究ノート** として書く。百科事典の説明文や、クエストの案内文（です・ます）にしない
- 同一ページ内で敬体・常体を混ぜない
- 英語原文の `you` は **「あなた」にしない**。魔導師が自分の発見を書き残した一人称寄りの文にする
- 主語は **省略が基本**（「発見した」「作成した」「ようだ」）。「私」は発見を強調するときだけ
- ためらい・余韻（`...` `だろう` `ようだ` `えー...`）は原文の独白なので落とさない
- 性能数値は `落下ダメージ軽減: 25%。` のような箇条書きにせず、地の文に溶かす（例: `落下ダメージは25%ほど軽減されるようだ。`）
- 思考の切れ目では本家に合わせて `<BR>` を使ってよい（原文に無くても、独白の段落として自然なら）
- アイテム名・研究名は既存 `ja_JP.lang` と ParaTranz Terms に合わせる（独自訳を増やさない）

中国語訳は `你`（二人称）のまま残すことが多い。日本語だけ一人称寄りに寄せる。

## 人称の変換

英語原文は二人称の研究日誌（`You have discovered...`）。日本語は次のように落とす。

| EN | JA |
|----|----|
| You have discovered a way to... | 〜する方法を発見した。 |
| You have become more efficient... | より効率的に〜できるようになった。 |
| After long research, you have managed to... | 長い研究の末、〜を発明した。 |
| you believe it to be worth the cost | それでも価値があるはずだ。 |

「あなたは〜できます」はクエスト口調なので使わない。

## キーの役割

| キー | 役割 | 口調 |
|------|------|------|
| `tc.research_name.*` | 研究名 | 原文の研究タイトルに合わせる。短い |
| `tc.research_text.*` | サブタイトル | 原文のダジャレ・一言を残す。常体でも、くだけた一言でも可 |
| `tc.research_page.*` | 本文 | **常体独白** |

研究名とアイテム名が英語でも違うことがある（例: 研究 `Feather Wings` / アイテム `Feather Duct-Taped Wings`）。

- **研究名は研究タイトルを訳す。** アイテム正式名へ勝手に置き換えない
- 本文のアイテム名は、タブによって書き方が違う（次節）
- 研究名とアイテム名が英語で同じなら、研究名もアイテム訳に揃えてよい（例: `Thaumium Reinforced Wings` → 魔導金属で強化された翼）

dreamcraft には `TConstruct.research_page.*` / `Minecraft.research_page.*` / `Forestry.research_page.*` / `WARPTHEORY.research_page.*` / `tb.rec.*.page.*` もある。本文の口調は同じ。

## 本文のアイテム名（タブで分ける）

**既定（魔術アドオン）** は和名だけを独白に溶かす。英語併記も `《》` も付けない。探究魔導学の「満たされた壺」「浮遊するろうそく」、秘術、神秘養蜂学、Gadomancy と同じ。

```text
ボール紙シートに羽根をダクトテープで貼り付け、翼の形に整える。悪くない考えに思えた。少なくとも、できた羽根の翼は、スペースキーを押せば空中へ体を押し出せる。
```

必要なら壺のように引用だけ使う（`'満たされた壺'`）。クエスト用の `§7《§r…》§r` は付けない。

対象の例: 電動魔具工学（EMT）、探究魔導学、秘術、Thaumic Tinkerer、Magic Bees など。

**例外: 新地平術タブ** のうち、他Mod・バニラの工業アイテムを解説するページだけ、既存どおり色なしの `《和名／English》` を使ってよい（苔の玉、ビーコン、シルキージュエル、TinyUranium）。NEI検索用。

```text
私は不要な 《ウラン238／Uranium 238》 を希少な同位体である 《ウラン235／Uranium 235》 へ変換する魔術的プロセスを発明した！
```

この例外を新規の魔術タブ本文へ広げない。

本体 Thaumcraft は `§5ソーモメーター§0`。本体ファイルを直すときは既存に合わせる。

## 改行・装飾コード（必ず保持）

クエストの `%n` や `[note]` は使わない。

- `<BR>` / `<BR><BR>` … 改行・段落
- `<LINE>` … 区切り線
- `<IMG>path:u:v:w:h:scale</IMG>` … 図版（数値は触らない）
- `§` 色・書式コード（本体 TC の `§5` アイテム名、`§n` 見出しなど）

DeepL 利用時はこれらが落ちやすいので、原文と必ず突合する。

## 用語の揃え（魔術まわりの例）

本体 Thaumcraft `ja_JP` に合わせる。

| 英語 | 採用 |
|------|------|
| Thaumonomicon | ソーモノミコン |
| Thaumometer | ソーモメーター |
| crucible | るつぼ |
| Infusion | 注入 |
| vis | Vis（カタカナ化しない） |
| essentia | エッセンシア |
| Salis Mundus | サリス・ムンドゥス |
| warp | 歪み |
| wand / cap / staff | 杖 / 石突 / 上級杖 |
| thaumium | 魔導金属 |
| primal aspect | 根源相 |
| compound aspect | 合成相 |
| aura node | オーラ節 |

数値（4桁以上）はクエストと同じく **半角カンマ区切り**（例: `10,000` LP）。`tick` もラテン字のまま。

## 手元マーク（検索用・手元ブランチのみ）

自分が訳した行をあとから拾いやすいよう、**`research_name` の先頭**に次のいずれか **1つ** を付ける。`research_text` / `research_page` には付けない。重ね書きしない（`[下書き]` → `[自訳]` → `[提出済み]` と置き換える）。

| マーク | 意味 | 検索 |
|--------|------|------|
| `[下書き]` | ゲーム未確認、または文言が未確定 | 作業中 |
| `[自訳]` | ゲームで見て手元では確定 | 投稿待ち |
| `[提出済み]` | ParaTranz に投稿した | 自分の投稿分 |

- 例: `tc.research_name.TinyUranium=[下書き]とても小さなウラン235`
- ゲーム内タイトルにも出る。公式訳と区別するための印
- **ParaTranz へ貼る文面からはマークを外す。** 手元ファイルには残して検索できるようにする
- 検索例: エディタで `[下書き]` / `[自訳]` / `[提出済み]` をファイル内検索

## 作業フロー

1. 訳は **ParaTranz** が本番。手元ブランチは下書き・用語揃え用
2. 手元の dreamcraft `ja_JP.lang` を編集 → `./sync-verified-thaums.sh`（クエストとまとめてなら `./sync.sh`）→ **完全再起動**してソーモノミコンで確認
3. `[下書き]` の間は、訳文の直前に比較用の英語原文をコメントで残す
   - `# EN name: ...`
   - `# EN text: ...`
   - `# EN page: ...`
   - コメント直後に空行を入れない
4. ゲーム確認後、`[下書き]` を `[自訳]` にし、対応する英語原文コメントを削除する
5. **見た目・文言が確定してから** git commit / push（下書き段階ではコミットしない）
6. ParaTranz へ確定文を投稿したら、手元の `[自訳]` を `[提出済み]` にする

`./sync-verified-thaums.sh` は dreamcraft の `ja_JP.lang` を 2.8.4 インスタンスへ上書きする。ゲームが見るのは `forceload`（TX-Loader 1.8.5）。`./sync.sh` でクエストと一括、`./sync.sh thaums` でこれだけ。

## レビュー観点チェックリスト

- [ ] 敬体（です・ます）になっていないか（クエスト口調の混入）
- [ ] `you` が「あなた」になっていないか
- [ ] 直前・同タブの既存日本語ページと口調が揃っているか
- [ ] 用語が本体 Thaumcraft / Terms と一致しているか
- [ ] `<BR>` / `<IMG>` / `§` が欠けていないか
- [ ] 《》にクエスト用の `§7` を付けてしまっていないか
- [ ] 魔術タブ本文に `《和名／English》` を付けてしまっていないか（新地平術の工業アイテム解説以外）
- [ ] サブタイトル（`research_text`）のダジャレを殺していないか
- [ ] 研究名をアイテム正式名で上書きしていないか（英語で短いタイトルなら短く訳す）

## 実績例: TinyUranium

キー: `tc.research_page.TinyUranium`

EN:

```text
After processing all your ores and using them for the creation of nuclear reactors, you have finally run out of uranium nuggets, needed to make your beloved fuel rods. After long research sessions, you have managed to transform your leftover uranium into much-needed nuggets!<BR><BR>Unfortunately, this process is a bit wasteful, but you believe it to be worth the cost.
```

JA:

```text
全ての鉱石を処理し終え、原子炉の核燃料を作成しようとしたが、あることに気が付いた。どうやらいくつかの素材が足りていないようだ。長い研究の末、私は不要な 《ウラン238／Uranium 238》 を希少な同位体である 《ウラン235／Uranium 235》 へ変換する魔術的プロセスを発明した！<BR><BR>残念なことに、このプロセスには無駄が多く、いくつかのロスが発生するが...それでも価値があるはずだ。
```

参照にした既存訳: 本体 `tc.research_page.RESEARCHER1.1`（「発見した」型）、dreamcraft `tc.research_page.UrnGTNH` / `TalismanfoodtGTNH`
