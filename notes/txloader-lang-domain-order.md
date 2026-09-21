# txloader のリソースドメイン走査順と、Mod同梱 ja_JP.lang に翻訳が負ける問題

調査日: 2026-09-08
対象環境: GTNH 2.8.4 インスタンス / txloader **1.8.5** / 翻訳パックは 2026-03(forceload時代) と 2026-07(load移行後) が混在

---

## 1. 症状

Thaumonomicon の一部ページが日本語にならない。翻訳ファイル側には訳があるのに反映されない。

```
魔導学タブ「Basic Wandcraft」の項目が名前・説明・本文すべて英語
  → tc.research_name.BASICTHAUMATURGY
```

一方で同じ魔導学タブの別項目は日本語になる。

```
tc.research_name.NODESTABILIZER = 節安定器   ← 正常
```

「所々だけ英語」という中途半端な出方をする。

---

## 2. 仕組み(バイトコードで確認済み)

### 2-1. txloader はフォルダ名を解釈しない

`glowredman/txloader/TXResourcePack`:

```java
// getResourceDomains() — フォルダ名をそのまま返す(HashSet)
dir.toFile().listFiles(DirectoryFileFilter.DIRECTORY)
   → new HashSet<>(); for each: set.add(file.getName());

// getResourcePath(ResourceLocation)
dir.resolve(location.getResourceDomain())      // ← ドメイン名 = フォルダ名そのもの
   .resolve(location.getResourcePath());
```

jar内の全クラスの文字列定数を走査したが、`[` を扱う正規表現も split も replace も無い。
`MinecraftClassTransformer` は `Minecraft.refreshResources` / `reloadResources` にフックして
Forceパックをリスト末尾に足すだけ(`MinecraftHook.insertForcePack`)。

つまり `Thaumcraft[thaumcraft]` は **文字通り `Thaumcraft[thaumcraft]` という名前のリソースドメイン**であり、
modid とは無関係。

### 2-2. なぜそれで動くのか

`Locale.loadLocaleDataFiles`(難読化 `brs.a`):

```java
for (String lang : ["en_US", 選択言語]) {
    String path = String.format("lang/%s.lang", lang);
    for (String domain : resourceManager.getResourceDomains()) {   // 全ドメインを走査
        loadLocaleData(resourceManager.getAllResources(new ResourceLocation(domain, path)));
    }
}
```

**全ドメインの lang ファイルを1つのグローバルなテーブルにマージする。**
ドメイン名が modid と一致している必要はなく、キーさえ合えば効く。
だからブラケット名でも動くし、アドオンが別フォルダから他Modのドメインへキーを足すこともできる。

**後に走査されたドメインが勝つ。**

### 2-3. 走査順の決まり方

`SimpleReloadableResourceManager`(難読化 `brg`):

```java
private final Set e = Sets.newLinkedHashSet();   // ← LinkedHashSet
```

`LinkedHashSet` なので **最初に挿入された時点で位置が確定**し、後から同じ名前で登録しても動かない。
挿入順はリソースパックの登録順:

1. vanilla の default パック
2. FML の Mod用リソースパック群(ここに **txloader の Normalパック = `load/`** も含まれる)
3. ユーザー選択のリソースパック
4. **txloader の Forceパック = `forceload/`** (フックでリスト末尾に追加)

### 2-4. 競合が起きる条件

- **Modが自前の ja_JP.lang を同梱していない** → 競合なし、翻訳パックが確実に反映
- **Modが自前の ja_JP.lang を同梱している** → `thaumcraft` と `Thaumcraft[thaumcraft]` という
  2つの別ドメインが同じキーを定義し、後に走査された方が勝つ

`forceload` の優先度が高いことはこの勝負に効かない。優先度は「同じドメイン・同じパス」を
複数パックが持つときの決着方法であって、ドメインが違えば別リソースとして両方読まれるため。

---

## 3. 実測データ

### Thaumcraft の内訳

`Thaumcraft-1.7.10-4.2.3.5a.jar` の `assets/thaumcraft/lang/ja_JP.lang` は
**1,191キー中517キー(43%)が英語のまま**。

翻訳パック `Thaumcraft[thaumcraft]` の1,549キーを突き合わせると:

| 状態 | キー数 | ゲーム内 |
|---|---:|---|
| jarのja_JPに存在しない | 378 | 翻訳パックが反映 (NODESTABILIZER はここ) |
| jarのja_JPが日本語 | 670 | jar側の訳が表示(パックの訳は無視) |
| jarのja_JPが英語 | **495** | **英語が表示** (BASICTHAUMATURGY はここ) |

### 影響を受ける全Mod

jar同梱の ja_JP.lang を持つのは22Mod。うち競合が発生するのは13ドメイン、**計1,214キー**。

| modid | jarのja_JP総数 | うち英語 | 競合キー | forceloadのフォルダ | load/にも同名 |
|---|---:|---:|---:|---|---|
| thaumcraft | 1,191 | 517 | **495** | `Thaumcraft[thaumcraft]` | あり |
| tinker | 941 | 437 | **434** | `Tinkers' Construct[tinker]` | あり |
| forbidden | 253 | 155 | **151** | `Forbidden Magic[forbidden]` | あり |
| projectred | 514 | 47 | 38 | `ProjectRed Core(+8)[projectred]` | なし |
| botania | 1,483 | 44 | 26 | `Botania[botania]` | あり |
| galacticraftcore | 697 | 190 | 16 | `Galacticraft Core(+1)[galacticraftcore]` | なし |
| biomesoplenty | 419 | 20 | 15 | `Biomes O' Plenty[biomesoplenty]` | あり |
| galacticraftasteroids | 133 | 53 | 13 | `Galacticraft Core(+1)[...]` | なし |
| galacticraftmars | 163 | 41 | 11 | `Galacticraft Core(+1)[...]` | なし |
| forestry | 827 | 324 | 7 | `Forestry[forestry]` | あり |
| cofh | 181 | 88 | 6 | `CoFH Core[cofh]` | あり |
| serverutilities | 276 | 35 | 1 | `ServerUtilities[serverutilities]` | あり |
| enderstorage | 8 | 1 | 1 | `EnderStorage[enderstorage]` | あり |

---

## 4. 決め手: `load/` に同名フォルダがあるかどうか

`load/` にも同名のブラケットフォルダがあると、そのドメインは **Normalパック(早い位置)** で
位置が確定してしまい、Mod自身のドメインより前に走査されて負ける。
`forceload/` にしか無ければ **Forceパック(最後)** が最初の宣言者になり、最後に走査されて勝つ。

実機で検証(2026-09-08):

| フォルダ | load/重複 | 予測 | 実測 |
|---|---|---|---|
| `ProjectRed Core(+8)[projectred]` | なし | 翻訳が勝つ | **「LXアップグレード」** ✅ |
| `Thaumcraft[thaumcraft]` | あり | jarが勝つ | **「Basic Wandcraft」** ❌ |

仮説どおりだった。

---

## 5. 適用した対処

**フォルダ名は一切変更していない。** `load/` 側の重複を退避しただけ。

1. `load/` にしか無かったキー28件を先に `forceload/` の同名ファイルへ追記
   - `Tinkers' Construct[tinker]` 18キー(パーツチェスト 等)
   - `Botania[botania]` 4キー(フラワーポーチ、任意の種 等)
   - `ServerUtilities[serverutilities]` 6キー(メインインベントリ、エンダーチェスト 等)
2. 重複していた9フォルダを `config_backup/txloader/load/` へ退避

結果、対象13ドメインすべてが「forceloadのみ」になり、**1,136キーが解放**
(thaumcraft 495 / tinker 434 / forbidden 151 / botania 26 / biomesoplenty 15 /
forestry 7 / cofh 6 / serverutilities 1 / enderstorage 1)。
projectred と galacticraft×3 の78キーは元から勝っていたので対象外。

**確認済み: Thaumonomicon のページが日本語になった。**

---

## 6. 上流の経緯 — なぜ `load/` へ移行しているのか

### TX-Loader PR #19「Inject non-force Resources later」(2025-12-16 merged / **1.8.7** で配布)

> Currently, the non-forced resources are loaded as if they were TX Loader's mod assets.
> **Due to this mod having a coremod, they are very early in the list.**
> This PR changes that. They are now placed **immediately before the user-selected resource packs**.
> This means that assets put in `./config/txloader/load/` **now override other mod's resources too**
> (previously, one had to use `./config/txloader/forceload/` which had the effect that resource packs
> could no longer be used for these resources). **This especially affects ParaTranz projects.**

本調査でバイトコードから導いた機序が、作者の言葉でそのまま説明されている。
1.8.7 で Normalパックの注入位置が後ろへ移り、Modのjarより後に走査されるようになった。

### GTNH-Translations PR #65「Move ParaTranz translations from forceload/ to load/」(2026-05-24)

> TX-Loader 1.8.7+ (PR TX-Loader#19) made `load/` override mod jars.
> ParaTranz translations were in `forceload/` alongside `____gtnhoverridenames`,
> **competing at the same priority level with no guaranteed order (HashSet)**.
> Moving them to `load/` leaves `forceload/` exclusively for override names,
> fixing items like **Obzinite showing the old Alumite name in Russian**.

移行の狙いは2つ:

1. `forceload/` 内で翻訳パックと `____gtnhoverridenames` が同優先度で衝突し、
   HashSet順という保証のない順序で勝敗が決まっていた問題の解消
   (= 今回インスタンスで踏んだ `(+N)` 重複と同じ構造の問題を、上流も独立に踏んでいた)
2. `forceload/` は何よりも強いため、ユーザーのリソースパックで翻訳を差し替えられなくなる
   (TX-Loader #20 の苦情) のを避ける

### GTNH-Translations PR #69「remove duplicate」(2026-05-27)

`forceload/` に残っていた旧ツリーを削除。以降 `forceload/` は
`____gtnhoverridenames` と `betterquesting` の2つだけになる。

### GTNH-Translations PR #80「Keep full mod-name folder in load path」(2026-06-22)

> PR #65 moved files from `forceload/` to `load/` but **also added a regex that stripped the folder
> name down to the bare resource domain**, so `Advanced Solar Panels[advancedsolarpanel]` became just
> `advancedsolarpanel`. The only change actually needed was `forceload` → `load`.
> **This restores the full folder name** so it stays consistent with how paths are uploaded to ParaTranz.

一時は素のドメイン名になっていたが、**ParaTranzのパス整合性のため意図的にブラケット名へ戻された**。
正しさの問題ではなく運用都合。

### 却下された修正案 — TX-Loader PR #27「Resolve resource domains from bracketed folder names」

ブラケット名から本来のドメインを取り出して解決する案。**却下**。

> **the bracketed folder names are load-bearing, not decorative.** Minecraft merges .lang translations
> by iterating getResourceDomains() and loading each reported name's lang file separately, which is how
> a mod's own folder and an addon's separate contribution to the same real domain both get merged today.
> Reporting the extracted domain instead of the bracket name collapses multiple contributing folders
> down to one reported domain, so only one of them would ever get resolved,
> **silently dropping the other's translations.**

ブラケット名はアドオンが他Modのドメインへキーを足すための意図的な設計であり、畳んではいけない。

### GTNH-Translations PR #92 (2026-07-23)

markdownツールチップだけを素のドメインへ逃がし、`.lang` の仕組みには手を触れない形で決着。

---

## 7. 結論

- **上流の 2.9(txloader 1.9 + load配置)ではこの問題は起きない。** PR #19 で解決済み
- 今回の症状は **txloader 1.8.5 に load移行後の翻訳パックを組み合わせた場合**に限定される
  - 1.8.5 では `load/` はまだ「早い位置」にあり、Modのjarを上書きできない
  - インスタンスの forceload(2026-03導入・forceload時代の配布物) と
    load(2026-07導入・load移行後の配布物) が混在していたのが直接の原因
- **上流へのIssueは不要**。強いて言えば「txloader 1.8.6以前と現行パックの組み合わせは非対応」
  という互換性の注意書き程度で、2.8.4を現行パックで遊ぶ人固有の事情
- 恒久対処の選択肢として **txloader を 1.8.7 以降へ差し替える**方法もある。
  そうすれば `load/` が本来の動作になり上流と同じ構成に戻せるが、他の挙動も変わる。
  現状の forceload 一本化で問題なく動いているならこのままでよい

---

## 参照

- TX-Loader: PR #19 (merged), PR #27 (closed), Issue #20 (closed)
- GTNH-Translations: PR #65, #69, #80, #92 (all merged), Issue #75, #8
- リリース: txloader 1.8.5(2025-05-29) / 1.8.6-pre(2025-10-10) / **1.8.7(2025-12-16)** / 1.9(2026-09-02)

---

## 8. セットアップスクリプト

新しく2.8.4インスタンスを立てたときは `./setup-instance.sh` 一発で同じ状態にできる。
実体は `tools/setup_instance_2_8_4.py`。冪等なので何度流しても安全。

```
./setup-instance.sh --dry-run     # 変更内容の確認
./setup-instance.sh               # 適用
INSTANCE_MC=/path/to/.minecraft ./setup-instance.sh
```

処理は3段階:

| Step | 内容 |
|---|---|
| A | `forceload/` 内で同一ドメインの重複フォルダを1つに集約。捨てる側にしか無い日本語キーは事前にマージ |
| B | 各 lang を再構築。キーはインストール済みjarの `en_US` ＋既存パックのキー、値は 最新訳 > 既存 > 英語。書式指定子が合わない訳は採用しない |
| C | Mod自前 ja_JP を持つドメインについて、`forceload/` と重複する `load/` フォルダを退避（本文書の主題の対処） |

**非langガード**: テクスチャ等を含むフォルダは Step A の対象外。
`forceload/betterloadingscreen` は lang を1つも持たず `textures/backgrounds/*.png` だけを
持つフォルダで、これを退避するとローディング画面が紫黒に化ける(実際に一度やらかした)。

除外ドメイン: `betterquesting`(クエスト本文は `sync-verified-quests.sh` の管轄)、
`minecraft`(バニラのドメインをModのスタブで再構築してはいけない)。

移動・書き換えたものは全て `config_backup/txloader/` 以下に退避される。

### 既存の sync スクリプトとの関係

`sync.sh` (= `sync-verified-quests.sh` + `sync-verified-thaums.sh`) との干渉を確認済み。

- **quests**: `merge_quest_lang_overlay.py` は `betterquesting.quest.<id>.(name|desc)` だけを
  差し替え、他の行は1行も変えない非破壊マージ。失われるキーは0
- **thaums**: `cp -a` による全上書きだが、リポジトリ側とインスタンス側で
  キー1,891/1,891・値差0の完全一致だったため実質 no-op

実行順は **`setup-instance.sh` → `sync.sh`**。

### 翻訳パックを再導入したら再実行が必要

インスタンスに書き込むスクリプトは `sync*.sh` の4本だけで、`main.py` はインスタンスを触らない。
危険なのは**翻訳パックそのものの再導入**で、再構築したファイルが上書きされ、
退避したフォルダが復活する。その場合は `./setup-instance.sh` を流し直せば元に戻る。

### 適用実績 (2026-09-08)

| | |
|---|---|
| Step A | 3フォルダ退避 (CB4BQ / alchemicalwizardryBooks / betterquesting。BQのUI文字列236キーはマージ) |
| Step B | 8ドメイン再構築 |
| Step C | 15フォルダ退避 (先行9 + 追加6)。合計47キーを事前マージ |

Step C の追加6ドメインは「英語で負け」は0件だったが、**jar同梱の古い訳が表示され
翻訳パックの訳が無視されていた517キー**をパック側に揃えた。

```
tile.appliedenergistics2.BlockCellWorkbench.name   セル作業台 → セルワークベンチ
item.railcraft.cart.anchor.name                    アンカー付きトロッコ → アンカー付きのトロッコ
options.showConflicts (Controlling)                競合を表示 → 被りを表示
```

最終状態: forceload 237 / load 269、Mod自前ja_JPとの競合ドメインは0。
jar実キー59,884中47,748(79%)が日本語。

---

## 9. Step D: 接頭辞が変わったキーの補正 (2026-09-21 追加)

### 症状

GT: New Horizons の `Steel Bars` が日本語にならない。訳は存在する。

```
2.8.4 のjar (GTNewHorizonsCoreMod-2.7.268.jar)
    item.SteelBars.name = Steel Bars       ← ゲームが引くキー
翻訳ファイル(インスタンス・上流とも)
    tile.SteelBars.name = スチールの格子     ← 訳が付いているキー
```

ブロックなので 2.8.4 より後に `item.` → `tile.` へ直された。翻訳は新しいキーに追従しているため、
**2.9では正しく出るが 2.8.4 では引かれない**。上流の `NewHorizonsCoreMod` master でも `tile.` 側。

Step B の再構築は「jarのキー ＋ 既存キー」で組むので、キー名そのものが変わった場合は拾えない。
接頭辞だけの違いなら機械的に補えるので Step D を追加した。

### 処理

各 forceload フォルダについて、jarの `en_US` が持つキーが未訳で、`item.` ⇔ `tile.` を入れ替えた
キーに日本語があれば、jarが引く側のキーへ訳文をコピーする(同一ドメイン内のみ、書式指定子チェックあり)。

### 適用実績 (2026-09-21) — dreamcraft 10件

| jarが引くキー | 訳の出どころ | 訳 |
|---|---|---|
| `item.AluminiumBars.name` ほか格子8件 | `tile.*Bars.name` | アルミニウムの格子 など |
| `item.SteelBars.name` | `tile.SteelBars.name` | スチールの格子 |
| `tile.MysteriousCrystal.name` | `item.MysteriousCrystal.name` | 奇妙なクリスタル |

格子9件は `item.` → `tile.`、`Mysterious Crystal` だけ逆方向(`tile.` → `item.`)。
全Mod横断で調べた結果、該当はこの10件のみ。

### 残った未訳 (対応不要)

`item.TungstenBars` `item.RedstoneAlloyBars` `item.ElectricalSteelBars` `item.ConductiveIronBars`
`item.EnergeticAlloyBars` `item.VibrantAlloyBars` `item.PulsatingIronBars` `item.SoulariumBars`
`item.EnderiumBaseBars` `item.EnderiumBars` の10件は英語のまま。
**2.9 では削除済みのキー**(上流の Bars キーは9件でいずれも訳済み)なので、
[[feedback_translation_version_scope]] の方針どおり翻訳対象にしない。

