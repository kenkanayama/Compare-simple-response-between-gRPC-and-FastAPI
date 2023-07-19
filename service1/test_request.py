import time
import grpc
import helloworld_pb2
import helloworld_pb2_grpc

def run():
    # サーバーとの接続を作成します
    channel = grpc.insecure_channel('localhost:50051')

    # チャネルを使用してスタブを作成します
    stub = helloworld_pb2_grpc.GreeterStub(channel)

    # リクエストを作成します
    request = helloworld_pb2.HelloRequest(name='Alice')

    time_sta = time.time()
    # RPCを呼び出し、レスポンスを取得します
    response = stub.SayHello(request)

    # print("Greeter client received: " + response.message)
    # 時間計測終了
    time_end = time.time()
    # 経過時間（秒）
    tim = time_end- time_sta
    print("経過時間（秒）：",tim)

if __name__ == '__main__':
    run()
