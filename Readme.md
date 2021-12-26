# Vueプロジェクトの作成&設定

## プロジェクトの設定
* コンテナに入って
  <pre>vue init webpack XXXX</pre>

## Vueプロジェクトをローカルで動かすために
### config/index.js
* 16行目
  * host: '0.0.0.0',
* 21行目
  * poll: true

## Vueのレスポンスが遅い件
* node_modulesをwatchしてるからっぽい
### build/webpack.dev.conf.js
* 44行目に追加
  * ignored: /node_modules/,

## Vueの起動
* コンテナに入って
  <pre>yarn run dev</pre>

## Vueで入れているライブラリ
* Vuetify
* vue-axios
* vue-toasted

# Fast-API

## Fast-APIの起動
* コンテナに入って
<pre>uvicorn app:app --host 0.0.0.0 --port 3000 --reload</pre>

## Fast-APIのDod
<pre>http://localhost:3000/docs</pre>

## 参考URL
* https://zenn.dev/sh0nk/books/537bb028709ab9/viewer/86648d