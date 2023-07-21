# 起動

>docker-compose build --no-cache

>docker-compose up -d

・gRPCサーバーを起動する
>docker-compose exec python-grpc-server sh

・fastAPIサーバーを起動する
>docker-compose exec python-fastapi-server sh

# テスト
・それぞれのサーバーで以下を実行する

>test_request.py

それぞれのサーバーからのレスポンス内容は同じ。

それぞれのサーバーのレスポンス時間とレイテンシーの確認ができる