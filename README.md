# notify-slack-of-qiita-with-lambda

> Qiitaのトレンド記事Top20を、Slackのチャンネルに投稿するLambda functionです。  
> Slack側で「incoming-webhook」を事前に設定する必要があります。  
> Pythonは3.7.0を使用しています。

## Setup

> 以下のコマンドで必要なライブラリをインストールします。

``` bash
$ pip install requests beautifulsoup4 -t .
```

## デプロイ

> このフォルダをzip化（ライブラリも含む）し、Lambdaにアップロードします。

## Lamda側の設定

> 以下の環境変数を設定します。

|キー |値 |
|---|---|
|webHookURL |[incoming-webhookに表示されたURL]|

> 最後に、CloudWatch Events等でスケジュール登録すれば、指定した時間にQiitaのトレンド記事Top20が通知されます。
