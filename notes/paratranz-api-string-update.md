# ParaTranz へ翻訳を一括投入する手順（検証記録）

調査日: 2026-09-10 / 対象プロジェクト: GregTech (`projects/8922`)

`gregtech-lang-migration-lost-translations.md` の復元作業で、GUI（Chrome拡張によるブラウザ操作）の代替として
ParaTranz の REST API を直接叩く経路を検証した。**動作するが、翻訳者としての貢献記録は付かない**（後述）。

## 認証

- `GTNH-Translations/.env` の `PARATRANZ_TOKEN` を `Authorization` ヘッダにそのまま入れるだけ。
  `Bearer` などのプレフィックスは不要。
- CSRFトークンやCookieは不要。ブラウザでのログインも不要。

```bash
TOKEN=$(grep '^PARATRANZ_TOKEN=' .env | cut -d= -f2- | tr -d '\r"')
curl -H "Authorization: $TOKEN" https://paratranz.cn/api/projects/8922
```

## 使うエンドポイント

| 用途 | メソッド / パス |
|---|---|
| プロジェクト情報 | `GET /api/projects/8922` |
| ファイル一覧 / 進捗 | `GET /api/projects/8922/files` , `GET /api/projects/8922/files/{fileId}` |
| 文字列一覧（ページング） | `GET /api/projects/8922/strings?file={fileId}&page={n}&pageSize=800` |
| 文字列1件取得 | `GET /api/projects/8922/strings/{stringId}` |
| **文字列1件更新** | `PUT /api/projects/8922/strings/{stringId}` |
| 変更履歴 | `GET /api/projects/8922/history?tid={stringId}` / `?uid={userId}` |
| メンバーと貢献数 | `GET /api/projects/8922/members` |
| ユーザー情報 | `GET /api/users/{userId}` |

存在しないもの（確認済み・すべて404）: `/api/users/me`, `/api/user`, `/api/me`,
`/api/auth/me`, `/api/notifications`, `/api/projects/{id}/strings/{sid}/history`。
**トークンの持ち主を問い合わせるAPIは無い。**

## 更新リクエスト

```bash
# ボディは UTF-8 の JSON ファイルに書いてから --data-binary で送る
# （シェル経由で日本語を直接埋めると環境によって化けるため）
curl -X PUT \
  -H "Authorization: $TOKEN" \
  -H "Content-Type: application/json; charset=utf-8" \
  --data-binary @body.json \
  "https://paratranz.cn/api/projects/8922/strings/1065602173"
```

`body.json`:

```json
{"translation": "鋳鉄製レンガ筐体", "stage": 1, "uid": 80161}
```

- `translation` … 訳文。UTF-8のJSONでそのまま通る（エスケープ不要、文字化けなし）。
- `stage` … `0`=未翻訳 / `1`=翻訳済み。新規投入は `1`。
- `uid` … 任意。**指定するとその文字列の翻訳者フィールドが該当ユーザーになる**（sivaDog = `80161`）。
  省略すると `null` になる。
- 成功時 HTTP 200 で更新後の文字列オブジェクトが返る。投入後に同じIDを `GET` すれば照合できる。

### キーの注意

TSVの `key`（例 `gt.blockmachines.hull.steel_bricked.name`）に対し、
ParaTranz側のキーは **`lang|` プレフィックス付き**（`lang|gt.blockmachines.hull.steel_bricked.name`）。
検索・突き合わせのときに必ずずれるので注意。

対象ファイル: `resources/GregTech[gregtech]/lang/ja_JP.lang.json` = `fileId 1171649`

## 【2026-09-21 追試】APIトークンでも `translate` + 自分のuidで記録された

下の 2026-09-10 の結論は **現在は再現しない**。InGameInfoXML (`fileId 1171670`) の
`lang|ingameinfoxml.config.showOnPlayerList` (`stringId 373938334`, 投入前 `translation=''` / `stage=0`) に対し、
`.env` の `PARATRANZ_TOKEN` で `PUT {"translation":..., "stage":1, "uid":80161}` を1件送った結果:

```
2026-09-21T13:39:10Z  op=translate  uid=80161  user=sivaDog  field=translation  to='プレイヤーリストに表示'
2023-12-10T11:21:48Z  op=import     uid=None                 field=original
```

2026-09-10 の GregTech 側 (`tid=1065602173`) は同じ形のリクエストで `op=import` / `uid=None` だったので、
**ParaTranz 側の挙動が変わったか、当時のリクエストに `uid` が乗っていなかったかのどちらか**。
再現条件の切り分けは未了。**ポイント加算も確認済み。** 続けて同じ経路で 23 件（新規22 + 上書き1）を投入した前後の `members`:

```
translated  606 -> 628  (+22 = 新規翻訳の件数)
edited      245 -> 246  (+1  = 既存訳の上書き)
totalPoints 2639.6 -> 2675.4  (+35.8)
```

`operation` は投入前の状態で決まる: 空 → `translate` / 既存訳あり → `edit`。どちらも `uid` と
`user.username` が入り、カウンタも該当する方が増える。**ブラウザ経路と区別が付かない。**

**運用上の結論:** 貢献記録が要るときも、まず API で1件送って `history` の `operation` を見る。
`translate` になるならブラウザ経路は不要。

## 重大な制約 — 貢献記録が付かない

> 以下は 2026-09-10 時点の記録。上の追試と矛盾するので、そのまま信用しないこと。

APIでの更新は、ParaTranzの変更履歴上 **`operation: "import"` / `uid: null`** として記録される。
GUI（ブラウザ）で翻訳した場合の **`operation: "translate"` / `uid: <ユーザーID>`** とは別扱い。

`GET /api/projects/8922/history?tid=1065602173` の実測:

```
2026-09-10T10:16:40Z  uid=None  op=import     field=translation  '鋳鉄製レンガ筐体'   ← API経由
2026-09-10T10:24:00Z  uid=46946 op=translate  field=translation  '超大型出力ハッチ'   ← GUI経由(別ユーザー)
```

- ボディに `uid` を入れると **文字列オブジェクトの `uid` は変わる**（＝その文字列の翻訳者表示は自分になる）。
- しかし **履歴エントリは `import` のまま新規作成されず、`members` の `translated` / `points` も増えない**
  （sivaDog: `translated 455` が uid付きPUTの前後で変化なし）。
- つまり **「自分が翻訳した」という貢献記録・ポイントを付けたいなら、APIでは不可能**。
  ブラウザのセッション（＝GUI操作、Chrome拡張経路）で入力する必要がある。

## 推奨手順 — ブラウザのログインセッション経由（`operation: translate` になる）

**Web UI は保存時に上と全く同じエンドポイントを叩いている。**
違いは認証方式だけなので、ログイン済みブラウザのページコンテキストから同じPUTを送れば
GUIをクリックして回るのと同じ扱い（`translate` + 自分のuid + 貢献ポイント）になる。

Web UI のバンドルから確認した実際の呼び出し:

```js
// 1件保存
this.$req.put(`/projects/${projectId}/strings/${id}`, {translation, stage})
// 一括保存
this.$req.put(`/projects/${projectId}/strings`, {op:`edit`, items:[{id, translation, stage}, ...]})
```

### やり方

1. Chrome で `https://paratranz.cn/projects/8922` を開きログインする。
   - ログイン確認: `fetch('/api/projects/8922/members/me',{credentials:'include'})` が
     **401 なら未ログイン / 403 ならログイン済み**（403でよい。このエンドポイントは元々叩けない）。
2. ページのコンテキストで `fetch` を回す。同一オリジンなのでCookieが自動で乗る。

```js
const H = {'Content-Type':'application/json'};
const xsrf = (document.cookie.match(/(?:^|;\s*)XSRF-TOKEN=([^;]+)/)||[])[1];
if (xsrf) H['X-XSRF-TOKEN'] = decodeURIComponent(xsrf);

// 投入直前に必ず現在値を確認し、空のときだけ書き込む（他の翻訳者との競合防止）
const cur = await (await fetch(`/api/projects/8922/strings/${id}`, {credentials:'include'})).json();
if (!(cur.translation||'').trim()) {
  await fetch(`/api/projects/8922/strings/${id}`, {
    method:'PUT', credentials:'include', headers:H,
    body: JSON.stringify({translation: tr, stage: 1})
  });
}
```

3. 1件ずつ逐次実行し、間に120ms程度のウェイトを入れる。83件で問題なく完走した（エラー0）。
4. 検証は `GET /api/projects/8922/history?tid={id}` で `operation` と `uid` を見る。

### 実測（2026-09-10）

```
op=translate  uid=80161  user=sivaDog   ← ブラウザセッション経由
op=import     uid=null                  ← APIトークン経由
```

貢献カウンタ: `translated 455 → 539`（+84）、`points 2329.4 → 2430.8`。

## セッションCookieを抜き出してブラウザ無しでやる案 — 非推奨

ParaTranzのセッションCookieは `sid` で、**HttpOnlyではない**ため JS から読める。
`curl -H "Cookie: sid=..."` でも同じ結果（`translate` 扱い）になるはずで、サーバ側に区別する手段はない。

ただし採用しない:

- **得るものが無い。** 上の手順は既にページ内で `fetch` を回しているだけで、GUI操作はしていない。
  curlに置き換えても速度は変わらず、違いは「Chromeが開いているか」だけ。
- `sid` はアカウント全体の権限を持つ生の認証情報。取り出すとシェル履歴・ファイル・ログに平文で残る。
- セッションなので期限切れ・ログアウトで失効し、CI等の長期用途には使えない。

## 使い分け

- **貢献記録が不要な機械的インポート** → APIトークン（`.env` の `PARATRANZ_TOKEN`、CI同期用）。
- **自分の翻訳実績として残したい** → ブラウザのログインセッション経由（上記）。

## 競合に注意

このプロジェクトは他の翻訳者がリアルタイムで作業している。実際、40分で32件が他者によって埋まっていた。
**投入直前に必ず現在値をGETし、空のものだけ書き込むこと。** 一括エンドポイントを使う場合も同様に事前確認が必要。

## 実施済み

- `gregtech-blockmachines-121-lost.tsv` の121件は投入完了（詳細は
  `gregtech-lang-migration-lost-translations.md` の「投入結果」を参照）。
