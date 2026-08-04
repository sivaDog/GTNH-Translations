# 日本語クエスト翻訳スタイルメモ（sivaDog）

ParaTranz / 手元ドラフト共通。既存の良い訳（とくに養蜂「巣枠」クエスト）に揃える。

## 口調

- クエストブック本文は **敬体（です・ます）**
- 同一クエスト内で敬体・常体を混ぜない
- アイテム名は Forestry 等の既存 `ja_JP.lang` に合わせる（独自訳を増やさない）

## 《和名／English》表記

既存訳の形式:

```text
§7《§r未加工の巣枠§7／Untreated Frame》§rは最も質素な巣枠です。
```

ルール:

- `§7《§r…§7／…》§r` を使う（直前の巣枠クエストと同じ）
- **マーカー直後・前後に半角スペースを入れない**
  - NG: `§r は、` / `§r よりも`
  - OK: `§rは、` / `§rよりも`
- 全角かっこ `（）`・全角スペースは使わない（表示崩れ）
- `§l`（太字）は極力使わず、強調は既存方針に合わせる（多くは `§n`）

## スペース（重要）

- **折り返し用の半角スペースは人が入れる。** AI／機械的な一括挿入はしない
- 下書きでは基本的に `》§rは` / `》§rを` / `》§rの` のように **助詞を直結**（巣枠クエスト型）
- 見た目調整のスペースは、ゲームで確認しながら人が判断する

## 用語の揃え（養蜂まわりの例）

| 英語 | 採用 |
|------|------|
| bee | **蜂**（「ミツバチ」にしない。既存クエストが「蜂」） |
| Untreated Frame | 未加工の巣枠 |
| Impregnated Frame | 含侵加工済み巣枠 |
| Proven Frame | 秘伝の巣枠 |
| Apiary | 養蜂箱 |
| Alveary | 大型養蜂箱 |
| Bee House | ビーハウス |
| GT scanner | **GregTechのスキャナー**（「GTのスキャナー」に略さない） |

時間単位 tick:

- Minecraft の時間単位はカタカナ「ティック」ではなく **ラテン字 `tick`**（既存クエストの `EU/tick`・`mB/tick`・`tick毎秒` に合わせる）
- 持続時間: `5,000 tick` / 毎tick: `毎tick`
- レート略記: `RF/t`・`EU/t` でよい（丁寧にするなら `RF/tick`）

数値（4桁以上）:

- 既存の丁寧訳に合わせ、**半角カンマ区切り**を使う（例: `1,000`・`16,000`・`480,000EU`・`50,000秒`）
- 原文の `1k` / `150K` のようなキロ略記は、**合計RFなど EN が K 表記のときだけ**踏襲してよい（例: 内燃エンジン `合計150K`）。tick 持続時間はカンマ区切りを優先（`1k ticks` → `1,000 tick`）
- 温度の `K`（ケルビン）と混同しやすいので、tick／RF のキロ略記を安易に増やさない

生産性の表現:

- 既存「巣枠」に合わせて **「倍にします」／「倍になります」**
- 「2倍にします」より、既存の「倍」に揃える方がよい

耐久などの比較:

- 「短めです」より説明文なら **「短いです」** の方が硬い（任意）

## 改行・装飾コード（必ず保持）

- `%n` / `%n%n` … 改行
- `[note]…[/note]` / `[warn]…[/warn]` / `[url]…[/url]`
- `§` 色・書式コード

DeepL 利用時はこれらが落ちやすいので、原文と必ず突合する。

## 下書きマーク（手元ブランチのみ）

自分が翻訳したクエストは、確定前はゲーム内で公式訳と区別できるよう **`name` の先頭に `[下書き]`** を付ける。確定後は **`[自訳]`** に変更する。`desc` には付けない。

- 例: `name=[下書き]含侵加工済み巣枠`
- ユーザーが訳を確定したら `[下書き]` を `[自訳]` に変更する（手元での確定版）
- ParaTranz へ投稿する確定文では `[下書き]` と `[自訳]` を外す

CustomToolTips は `ja_JP/config/txloader/load/customtooltips/lang/ja_JP.lang`（キー `customtooltip.*`）。locale 専用 XML は置かない（あると本体のキー化 XML より優先され lang が効かない）。値の先頭に `[下書き]` / `[自訳]` を付ける。

- 例: `customtooltip.bee_apiary=[下書き]有効生産確率…`

## 作業フロー（再掲）

1. 訳は **ParaTranz** が本番。手元ブランチは下書き・用語揃え用
2. 確認: `./sync-verified-quests.sh` → **ゲーム完全再起動**（ワールド再入場だけでは lang は載らない）
   - sync 対象は `notes/quest-ids-2.8.4.txt` にあるクエストのみ。章を増やすときはその ID リストへ追加する
   - `Coins, Coins, Coins` 章は 2.9+ で Vending Machine 化され upstream 対象外のため、翻訳作業対象に含めない
   - `初歩的な魔導学`（Novice Thaumaturgy / questline `AAAAAAAAAAAAAAAAAAAAFg`）は `notes/quest-ids-2.8.4.txt` 末尾に **103 ID** 追加済み（2.8.4 章 99 + master 整合の 4）。未訳一覧は `notes/novice-thaumaturgy-gap.txt`（英語のまま残っているものは約 57 件）
   - `交配の方蜂`（Be(e) Breeding / questline `AAAAAAAAAAAAAAAAAAAAEw`）は `notes/quest-ids-2.8.4.txt` に **170 ID** 済み。切り出しは `notes/quest-ids-bee-breeding.txt`、未訳一覧は `notes/bee-breeding-gap.txt`
3. `/bq_admin default load` はクエスト JSON 用。lang のリロードコマンドではない

## レビュー観点チェックリスト

- [ ] 直前・同章の既存日本語クエストと口調が揃っているか
- [ ] 《》のスペース有無が既存と一致しているか
- [ ] アイテム／生物の訳語が Terms・既存 lang と一致しているか
- [ ] `%n` と `§` / `[note]` 等が欠けていないか
- [ ] タイトルが章内の短さ（総称 vs 正式名）と極端にズレていないか

## 表示（クエストブックの折り返し）

`《和名／長い English》` が続くと、英単語の途中で改行され見づらい。

- **初出だけ《和名／English》**、2回目以降は和名のみ（既存「巣枠」クエストと同じ）
- 必要なら `%n` で《》の前後を切る

## 作業の進め方（確定まで）

- `[下書き]` の間は、訳文の直前に比較用の英語原文をコメントで残す
  - `# EN name: ...`
  - `# EN desc: ...`
  - `# EN desc:` の直後に空行を入れない（次行はすぐ `betterquesting.quest....name=`）
- 訳を確定して `[自訳]` に戻すときに、対応する英語原文コメントを削除する

1. 手元の `ja_JP.lang` を編集 → `./sync-verified-quests.sh` → ゲーム再起動で確認  
2. **見た目・文言が確定してから** git commit / push（下書き段階ではコミットしない）  
3. 公式反映は ParaTranz へ確定文を投稿

## upstream マージ後の `[下書き]` 復元

`origin/master` を `--theirs` で取り込むと、ParaTranz 未反映の `[下書き]` エントリは upstream 側に存在しないため消えます。マージ直後に次を実行してください。

```bash
./tools/restore_drafts_after_merge.sh
./sync-verified-quests.sh
```

`restore_drafts_after_merge.sh` は merge 直前の `HEAD^1`（作業ブランチ側）から `[下書き]` を読み、upstream ベースの `ja_JP.lang` へ **置換または新規挿入** します。`sync-verified-quests.sh` は同期前に `tools/check_quest_lang_coverage.py` で ID リストと lang の欠落を検査します。

消失の検証（`.desc=` / quest ID 件数比較）:

```bash
python tools/compare_quest_lang_snapshots.py \
  "backup-20260718=/path/to/_backup_ja_JP_.../load_betterquesting_ja_JP.lang" \
  "pre-merge=/tmp/pre-merge.lang" \
  "current=ja_JP/config/txloader/forceload/betterquesting/lang/ja_JP.lang" \
  --baseline pre-merge \
  --id-list notes/quest-ids-2.8.4.txt
```

`pre-merge.lang` は `git show HEAD^1:ja_JP/config/txloader/forceload/betterquesting/lang/ja_JP.lang` などで取得します。

## 実績例: Impregnated Frames

キー: `betterquesting.quest.AAAAAAAAAAAAAAAAAAAEWQ`

```text
name=[自訳]含侵加工済み巣枠
desc=§7《§r含侵加工済み巣枠§7／Impregnated Frame》§rは、未加工の巣枠よりもさらに優秀です。%n各巣枠は蜂の生産性を倍にします。耐久は未加工の巣枠より長く、秘伝の巣枠よりは短めです。
```

参照にした既存訳: `# Quest: Frames`（`AAAAAAAAAAAAAAAAAAAEWA`）
