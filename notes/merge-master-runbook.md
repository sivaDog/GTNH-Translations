# master → 作業ブランチ マージ手順書（エージェント向け）

作成: 2026-10-17 / 対象リポジトリ: GTNH-Translations のローカルクローン（このファイルがあるリポジトリ）

本家（GTNewHorizons/GTNH-Translations）の更新を、ローカルの `master` に取り込み、
それを作業ブランチ `work/sivaDog-translations` にマージする手順。
2026-08〜10 に実際に起きたトラブルと、その時の判断をすべて反映してある。

---

## 0. 前提

| 項目 | 値 |
|---|---|
| OS / シェル | Windows 11、**Git Bash**（PowerShell ではない） |
| 作業ディレクトリ | 上記リポジトリのルート。**すべてのコマンドの前に `cd` すること** |
| `origin` | 本家 `git@github.com:GTNewHorizons/GTNH-Translations.git`（読むだけ） |
| `fork` | 本人のフォーク `sivaDog/GTNH-Translations`（**プッシュは本人がやる。エージェントはしない**） |
| `master` | `origin/master` の**単純なミラー**。独自コミットは無い。直接編集しない |
| 作業ブランチ | `work/sivaDog-translations`。本人の翻訳作業（下書き・提出済みマーカー付き）がある |
| 補助スクリプト | `tools/merge_master_helper.py`（この手順の自動化部分。`--help` で用法） |

### 翻訳ファイルのマーカー

作業ブランチの `.lang` には、本人が付けた進捗マーカーが値の先頭にある。

| マーカー | 意味 |
|---|---|
| `[下書き]` | 手元の下書き。まだ ParaTranz に出していない |
| `[自訳]` | 確定した自分の訳。まだ出していない |
| `[提出済み]` | ParaTranz に投稿済み。本家への同期待ち |
| `# EN name:` / `# EN desc:` などのコメント行 | 原文比較用のメモ |

本家（ParaTranz からの同期）が追いつくと、同じ訳がマーカー無しで `master` に入ってくる。
**マージ時のコンフリクトの大半は「マーカーの有無だけの差」**で、その場合は本家側を採用すればよい。

---

## 1. 絶対にやらないこと

- `git push`（どのリモートにも）。`--force` も当然しない
- 作業ブランチでの `git reset --hard` / `git checkout -- .` / `git restore .` / `git clean`
  （ワイルドカードで作業ツリー全体を戻すコマンドは全部禁止。戻すのは**名前を挙げたファイルだけ**）
- `git rebase`、`git commit --amend`、`--no-verify`
- 複数行のコミットメッセージ（本文や `Co-Authored-By` 行を付けない。**メッセージは1行**）。
  コンフリクトを解決した後の `git commit --no-edit` は `# Conflicts:` 行が残って複数行になるので使わない（8章の `-m` を使う）
- `git stash drop` / `git stash clear` を、復元内容を確認する前に実行すること
- `master` にコミットすること、`master` 上のファイルを編集すること
- `notes/` や `tools/` の未追跡ファイルを消すこと（本人の作業データ）
- `tools/restore_drafts_after_merge.sh` を実行すること
  （`[提出済み]` のブロックまで旧版で上書きし、改行もLFにするので、この手順の解決結果を壊す）
- 判断に迷うコンフリクトを推測で片付けること（→ 10章の条件で止まって人間に聞く）

---

## 2. 事前確認

```bash
cd "<GTNH-Translations のルート>"           # 実際のパスは依頼者に聞く。以後 git rev-parse --show-toplevel と一致すること
git branch --show-current          # work/sivaDog-translations のはず
git status --short | grep -v '^??' # 追跡ファイルの未コミット変更を確認
ls .git/MERGE_HEAD 2>/dev/null && echo "マージが途中のまま!"
git stash list                     # 既存の stash があれば控えておく（触らない）
```

- 現在のブランチが違う、`MERGE_HEAD` が残っている、`git stash list` に見覚えの無い新しい stash がある
  → **10章: 停止して報告**

## 3. 作業中の変更を退避（ある時だけ）

`git status --short | grep -v '^??'` に何か出たら、それは本人の作業中の変更。

```bash
git stash push -m "wip before master merge $(date +%F)"
git stash list | head -1
```

- **`-u` は付けない**（未追跡の `notes/` などは退避しない。マージには影響しない）
- 退避直後に `git status --short | grep -v '^??'` が空になったことを確認

## 4. 本家を取得し、`master` を追従させる

```bash
git fetch origin
git log master..origin/master --oneline | wc -l           # 取り込むコミット数（0なら6章へ進んでよいが、そのまま終了でもよい）
git merge-base --is-ancestor master origin/master && echo FF-OK || echo FF-NG
```

- `FF-NG` → 本家の履歴が書き換えられた（2026-07 に一度あった）。**10章: 停止して報告**

補助スクリプトは作業ブランチにしかコミットされていないので、**master に切り替える前に一時フォルダへ取り出す**
（取り出さずに master で `python tools/merge_master_helper.py` を実行すると「No such file」で止まる）。

```bash
H="$(python -c 'import tempfile;print(tempfile.gettempdir())')/merge_master_helper.py"
git show work/sivaDog-translations:tools/merge_master_helper.py > "$H"
git checkout master
python "$H" fix-tree                           # 大文字小文字アーティファクトの掃除（5章参照）
git merge --ff-only origin/master
python "$H" fix-tree
git status --short | grep -v '^??'             # 空であること
python "$H" dupes HEAD origin/master           # 0 であること
```

（作業ブランチに戻った後は `tools/merge_master_helper.py` を直接使ってよい。`$H` のままでも同じ。）

- `git checkout master` が「Your local changes ... would be overwritten」で失敗したら 9章の該当行へ
- `fix-tree` が "other changes left untouched" を出した場合、master に本物の変更があるのは異常
  → **10章: 停止して報告**

## 5. 大文字小文字アーティファクトについて（Windows 特有）

本家リポジトリには過去に、大文字小文字だけ違うパスが同時に追跡されていた
（例: `Witchery++[WitcheryExtras]` と `Witchery++[witcheryextras]`）。
Windows ではこの2つが同じ1ファイルになるため、ブランチ切り替えのたびに次の症状が出た。

- 何も編集していないのに `M`（変更あり）と表示される
- ファイルが `D`（作業ツリーから消えた）と表示される
- `checkout` が「Your local changes would be overwritten」で止まる

`python tools/merge_master_helper.py fix-tree` は、**衝突しているパスに限って** `M` を元に戻し、
`D` を HEAD から書き戻す（最大5周。戻すと反対側の綴りが `M` になる「反転」が起きるため）。
衝突パス以外の変更には触らず一覧表示だけする。

2026-10-13 時点で本家の重複は0件（本家に重複チェックのワークフローが入った）。
`python tools/merge_master_helper.py dupes HEAD origin/master` が 0 以外なら **10章: 停止して報告**。

## 6. 作業ブランチに戻ってマージ

```bash
git checkout work/sivaDog-translations
python "$H" fix-tree
git status --short | grep -v '^??'             # 空であること（3章で退避済みのため）
git merge master --no-edit                     # コンフリクト無しならここで1行メッセージのマージコミットができる
```

- コンフリクトが無ければ「Merge made by the 'ort' strategy.」→ 8章へ
- `CONFLICT (content): Merge conflict in ...` が出たら 7章へ
- 「untracked working tree files would be overwritten by merge」→ **10章: 停止して報告**

## 7. コンフリクトの処理

まず一覧を出す。

```bash
git diff --name-only --diff-filter=U
```

### 7-1. `.lang` ファイル

```bash
python tools/merge_master_helper.py lang --dry-run     # 分類だけ表示、何も書かない
```

スクリプトはコンフリクトの各ブロックを**キー単位**で、作業ブランチ側（user）と本家側（upstream）、
そして共通の祖先（git の stage 1）と比較して分類する。

| 分類 | 状況 | 自動で採用する側 |
|---|---|---|
| `MARKER_ONLY` | マーカー/`# EN` コメントを除けば同じ訳 | 本家（マーカー無し） |
| `USER_ONLY` | 作業ブランチにしかないキー（本家がまだ同期していない） | 作業ブランチ（マーカーごと残す） |
| `UPSTREAM_ONLY` | 本家にしかないキー | 本家 |
| `USER_DRAFT` | 作業ブランチは日本語、本家は英語のまま（未投稿の下書き） | 作業ブランチ（直上の `# EN` 行も残す） |
| `UPSTREAM_EN` | どちらも日本語ではない（英語原文の更新など） | 本家 |
| `UPSTREAM_CHANGED` | 作業ブランチはマーカーを付けただけで本文は祖先のまま。本家が本文を変えた | 本家 |
| `USER_CHANGED` | 本家は祖先のまま。作業ブランチが本文を変えた | 作業ブランチ |
| `CONFLICT` | **両方が本文を変えた** | **自動では決めない**（`UNRESOLVED` と表示） |

`UNRESOLVED` が無ければそのまま書き込む。

```bash
python tools/merge_master_helper.py lang
```

`UNRESOLVED` があるブロックはコンフリクトマーカーが残ったままになる（終了コード 3）。
表示された user / upstream の2つの訳を見比べ、**これまでの判断の前例（11章）では毎回本家側が採用されている**ので、
原則は本家側で解決する。ファイルとブロック番号を指定して再実行する。

```bash
python tools/merge_master_helper.py lang --force 2=upstream "ja_JP/config/txloader/forceload/betterquesting/lang/ja_JP.lang"
```

- `--force N=upstream` / `--force N=user` が効くのは、そのブロックの `CONFLICT` キーだけ。
  同じブロック内の下書きや未同期キーは通常どおり残る
- 原則から外れて**止まって聞く**のは次の場合（10章）:
  - 作業ブランチ側の訳に、本家側に無い**文や段落がまるごとある**（本家が古い・欠落している可能性）
  - 書式コード（`§l` 太字 / `§n` 下線 など）だけが違い、どちらが正しいか分からない
    （判断材料: 英語原文 `daily-history/**/en_US.lang` の同じキー。前例では英語原文に合わせた）
- `USER_DRAFT` で、本家の英語原文が `# EN` コメントの英語から変わっていたら、`# EN` 行を新しい英語に書き換えるとよい（任意）

ブロック分けは git の差分単位なので、1ブロックに数十キー入ることもある。分類はキーごとに出る。

### 7-2. `.lang` 以外（Python のソースなど）

自動解決しない。2026-10-13 に `src/gtnh_translation_compare/paratranz/client_wrapper.py` で実例あり。

1. 各側を誰が変えたか確認する
   ```bash
   git log --oneline -5 ORIG_HEAD..master -- <ファイル>      # 本家側の変更
   git log --oneline master..ORIG_HEAD -- <ファイル>         # 作業ブランチ側（本人）の変更
   ```
2. **片側を丸ごと採用しない**。両方の意図を残して手で統合する
   （前例: 本家は「429/500/504 をリトライ」、本人は「通信エラー全般をリトライ」→ 両方をリトライ対象にした）
3. 構文チェック
   ```bash
   python -m py_compile <ファイル>
   ```
4. テスト。`poetry` があれば `poetry run pytest tests/ -q`。無ければ（現状は pytest も poetry も未導入）
   **「テスト未実行」と報告に明記**する
5. 統合方針に自信が無ければ → 10章: 停止して報告

### 7-3. 解決後

```bash
git add <解決したファイルを1つずつ名前で>
git diff --name-only --diff-filter=U        # 空であること
python tools/merge_master_helper.py verify  # 8章
```

## 8. 検証してコミット

```bash
python tools/merge_master_helper.py verify
```

チェック内容: コンフリクトマーカーの残り、`.lang` の重複キー、CRLF→LF 化（`.lang` は CRLF）、
HEAD の大文字小文字重複、未解決ファイル。`verify: OK` でなければコミットしない。

**マージで持ち込んだ問題だけを見る。** 結果がどちらかの親と同一のファイルは対象外
（`note: N changed file(s) are identical to the master side` と出るのは正常）。
本家自体が LF のファイルや、本家の zh_CN にある重複キーなどは、マージのせいではないので NG にならない。

```bash
ls .git/MERGE_HEAD && git commit -m "Merge branch 'master' into work/sivaDog-translations"
git log --oneline -3
```

コンフリクト無しでマージが完了していた場合はコミット済みなので、`verify` だけ実行する
（その場合 `verify` は HEAD との差分を見るので「変更なし」で OK になる）。

## 9. 退避した変更を戻す（3章で退避した時だけ）

```bash
git stash pop
```

- 成功（`Dropped refs/stash@{0}`）→ `git status --short | grep -v '^??'` で作業中の変更が戻っていることを確認して完了
- `CONFLICT` が出た場合、**stash は自動では消えずに残る**（消さないこと）。
  stash のコンフリクトは表示の向きがマージと逆（上が「Updated upstream」= マージ済みの最新、下が「Stashed changes」= 作業中の変更）。

```bash
python tools/merge_master_helper.py lang --mode stash --dry-run
python tools/merge_master_helper.py lang --mode stash
```

  `--mode stash` では `CONFLICT`（両方が本文を変えた）は**作業中の変更（user）を優先**する。
  作業中の変更はマーカーを更新しただけ（`UPSTREAM_CHANGED`）なら最新側を採る。

```bash
python tools/merge_master_helper.py verify
git reset -q                                  # stash pop が付けたステージングを外し、元の「未ステージの作業中変更」に戻す
git stash show --stat stash@{0}               # stash の中身
git diff --stat                               # 戻った作業中変更
```

  2つの `--stat` で、stash にあったファイルがすべて作業ツリーに変更として戻っていることを確認してから:

```bash
git stash drop stash@{0}
```

- **部分適用の罠**（2026-09-04 に実際に起きた）: pop が途中で失敗し、一部のファイルだけ戻って
  残りは戻らないことがある。`git stash show --name-only stash@{0}` のうち、作業ツリーで変更になっていない
  ファイル（`git diff --quiet -- <file>` が成功するもの）は、HEAD と同じ内容なので、名前を挙げて取り出す。
  ```bash
  git checkout stash@{0} -- "<そのファイル>"
  git reset -q
  ```
  それでも stash と作業ツリーの差が説明できない場合は drop せずに 10章: 停止して報告

## 10. 停止して人間に聞く条件

以下のどれかに当たったら、それ以上進めずに、**ここまでの状態と出力を報告して待つ**。
途中の状態（コンフリクト中・stash 残り）はそのままでよい。勝手に `git merge --abort` もしない。

1. `master` が fast-forward できない（`FF-NG`）、または「refusing to merge unrelated histories」
2. 事前確認でブランチが違う / `MERGE_HEAD` が残っている / 見覚えの無い stash がある
3. master 上で `fix-tree` が衝突パス以外の変更を報告した
4. `dupes` が 0 以外（大文字小文字の重複パスが再発した）
5. マージが「untracked working tree files would be overwritten」で止まった
6. `.lang` の `CONFLICT` で、7-1 の「止まって聞く」場合に当たった
7. `.lang` 以外のコンフリクトで、統合方針に自信が無い
8. `verify` が NG のまま直せない
9. stash の復元内容が stash と一致しない
10. 同じコマンドを2〜3回やっても状況が変わらない（`fix-tree` の「still flipping」など）
11. この手順に書いていない状況全般

## 11. 判断の前例（本人が過去に下した決定）

| 日付 | 状況 | 本人の判断 |
|---|---|---|
| 2026-08〜 | マーカー/`# EN` コメントの有無だけの差 | 本家側（マーカー無し）を採用 |
| 2026-08 | EBF マニュアル: メンテナンスハッチ共有の可否で訳文が食い違い | 本家（ParaTranz）版を採用 |
| 2026-08-31 | クエスト名の書式コードが `§n`（下線）vs `§l`（太字） | 英語原文に合わせて本家版（`§l`） |
| 2026-09-04 | 「充電中…」: 作業ブランチだけ用語に `§7《§r日本語§7／English》§r` 装飾 | 本家（装飾なし）版を採用 |
| 2026-09-11 | 「憤怒種」: 同じく装飾の有無 | 前例どおり本家版 |
| 2026-09-09 | 本家は英語のまま、作業ブランチに `[下書き]` の日本語 | 作業ブランチ（下書き）を残す |
| 2026-10-08 | ServerUtilities: 作業ブランチにしか無いキー48件（本家未同期） | 作業ブランチを残す |
| 2026-10-13 | `client_wrapper.py`: 本家と本人が同じ関数を別々に修正 | 両方の意図を統合 |
| 2026-08-30 | stash 復元で、作業中の変更がマーカー更新（`[下書き]`→`[提出済み]`）だけ、本家は同期済み | 最新（本家同期済み）側を採用 |

## 12. 詰まった時の対処表

| 症状 | 原因 | 対処 |
|---|---|---|
| `git checkout master` が「Your local changes ... would be overwritten」 | 5章のアーティファクト | `fix-tree` → 再度 checkout。ダメなら 10章 |
| master で何もしていないのに `M` が十数件 | 5章のアーティファクト | `fix-tree` |
| 作業ブランチに切り替えた直後、`D` が20件前後 | 5章のアーティファクト（ファイルが書き出されなかった） | `fix-tree` |
| `fix-tree` を実行すると別の綴りのパスが `M` になる | 反転。2つの綴りが1ファイルを取り合っている | `fix-tree` は自動で5周する。それでも止まらなければ 10章 |
| `grep -c` が終了コード1 | 0件ヒット時の grep の仕様。エラーではない | 無視してよい |
| Python の出力が文字化け / `UnicodeEncodeError: 'cp932'` | Windows コンソールの文字コード | 補助スクリプトは対策済み。自作スクリプトは `sys.stdout.reconfigure(encoding="utf-8")` |
| Git Bash の heredoc で `\n` が実改行になる | Git Bash は `<<'EOF'` でもバックスラッシュを潰すことがある | スクリプトはファイルに書いてから実行する。`\n` の文字列は `chr(92)+"n"` で組む |
| `grep -P` が使えない | この環境の grep は UTF-8 ロケール非対応 | Python で処理する |
| `git rm --cached` などが権限分類器にブロックされる | 一括の破壊的操作とみなされた | 1ファイルずつ明示して実行。それでもダメなら 10章（回避策を探さない） |
| `.lang` を Python で書き直したら CRLF が LF になった | `open()` の改行変換 | 読み書きとも `newline=""` を指定する（補助スクリプトは対応済み）。`verify` で検出できる |
| `lang` が「no unmerged .lang files」 | すでに解決済み、または `.lang` 以外だけがコンフリクト | `git diff --name-only --diff-filter=U` を確認 |
| master で `python tools/merge_master_helper.py` が「No such file」 | スクリプトは作業ブランチにしか無い | 4章のとおり一時フォルダに取り出した `$H` を使う |
| マージコミットのメッセージに `# Conflicts:` 行が入った | コンフリクト解決後に `--no-edit` でコミットした | まだプッシュ前なら人間に報告（amend は禁止事項なので自分ではしない） |

## 13. 終わったマージを後から点検する（人間・別エージェント向け）

別のエージェントが行ったマージを確認する時は、作業ツリーを触らずに次を実行する。

```bash
git log --merges --format="%h %ad %s" --date=short -5 work/sivaDog-translations
python tools/merge_master_helper.py verify <マージコミットID>
python tools/merge_master_helper.py dupes HEAD
git status --short | grep -v '^??'; git stash list; ls .git/MERGE_HEAD 2>/dev/null
```

2026-10-25 に、Grok が行った 10/19 のマージ（`0f1262ec1`）をこの方法で点検し、問題なしを確認した。

## 14. 報告テンプレート

```
master: <旧> → <新>（取り込みコミット数 N）
マージ: <コミットID> / コンフリクト <件数>（ファイル別）
  自動解決: <分類ごとの件数>
  --force で解決したブロック: <ファイル> block <N> = upstream/user（理由・両側の訳）
  .lang 以外: <ファイル>（統合内容、py_compile 結果、テスト実行有無）
fix-tree: master <回数/件数>、作業ブランチ <回数/件数>
dupes: HEAD <n> / origin/master <n>
verify: OK / NG（内容）
stash: なし / 復元済み / 残置（理由）
プッシュ: していない（本人が実施）
停止した場合: 10章の何番に該当したか、そのときの状態
```
