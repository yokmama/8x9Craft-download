# hackCraft2

**hackCraft2** GitHubプロジェクトへようこそ！このプロジェクトは、Minecraftでプログラミングを可能にするプラグイン、**hackCraft2** のダウンロードファイルとリソースをホストしています。

## 目次
- [紹介](#紹介)
- [機能](#機能)
- [インストール](#インストール)
- [使用方法](#使用方法)

## 紹介
hackCraft2は、Minecraft内でプログラミングを可能にするプラグインです。hackCraft2を使用することで、カスタムスクリプトの作成、タスクの自動化、新しいゲームメカニクスの開発などが可能になります。

## 機能
- **インゲームスクリプティング**：Minecraft内で直接コードを記述して実行できます。
- **自動化**：繰り返し作業や複雑なプロセスを自動化します。
- **カスタマイズ**：カスタムゲームメカニクスやインタラクションを作成できます。
- **教育的**：楽しくインタラクティブな環境でプログラミングの概念を学べます。

## インストール
hackCraft2をインストールするには、以下の手順に従ってください：
1. java ランタイムインストール
    - https://docs.oracle.com/javase/jp/13/install/overview-jdk-installation.html
    - 推奨バージョン　17以上

2. paper minecraftインストール
    - https://papermc.io/
    - 編集時点 1.20.4

3. hackCraft2 plugin install
    - [リリースページ](https://github.com/yokmama/8x9Craft-download/tree/master/hackCraft2/plugins)から最新バージョンのhackCraft2をダウンロードします。
    - ダウンロードしたファイルをMinecraftサーバーの`plugins`ディレクトリにコピーします。
    - サーバーを再起動してプラグインを読み込みます。

## config.ymlの設定
サーバーを起動すると、自動でpluginsフォルダに hackCraft2というフォルダが生成されます。
そのフォルダにある、config.yml を変更してください。
```
host: localhost
http_port: 8080
http_enable: true
http_path: www
ws_host: localhost
monaco_port: 25569
monaco_enable: true
scratch_port: 25570
scratch_enable: true
openai_token: 
```
* host: リンクでクリックしたときに表示するWebサーバのホスト名です
* http_port: リンクでクリックしたときに表示するWebサーバのポート番号です
* http_enable: 内部Webサーバーを有効
* http_path: 内部Webサーバの公開フォルダ
* ws_host: hackCraft2が動作しているサーバーのホスト名です
* scratch_port: スクリプトAPIを提供するWebSocketのポート番号です
* monaco_port: レンダリングAPIを提供するWebSocketのポート番号です
* scratch_enable: スクリプトAPIを有効
* monaco_enable: レンダリングAPIを有効

## 使用方法
インストール後、以下の基本手順でhackCraft2を使用できます：

1. **ペットを捕まえる**：ゲーム内で/hack craftコマンドを使用してペットタグを入手し、そのペットタグで動物に名前をつけます。
2. **スクリプトを書く**：python環境でスクリプトを書き始めます。
```
from py2hackCraft.modules import Player

player = Player("<your minecraft name>")
player.login("<your host name>", <your port>)

hello = player.getEntity("hello")

for i in range(5):
    hello.forward()
    hello.turnRight()

player.logout()
```    
>port番号はデフォルトで **25570** です。これらは plugins/hackCraft2/config.yml で設定を変更できます。
くわしくはこちらを参照ください。(https://pypi.org/project/py2hackCraft2/)

3. **スクリプトを実行**：スクリプトを実行して、ゲーム内で効果を確認します。


---

質問がある場合やサポートが必要な場合は、[Issuesページ](https://github.com/yokmama/8x9Craft-download/issues)からお気軽にお問い合わせください。

hackCraft2でのコーディングをお楽しみください！
