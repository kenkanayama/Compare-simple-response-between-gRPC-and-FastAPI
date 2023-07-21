import time
import requests
import json

url = "http://localhost:8089/name/"

payload = {
    "name": "kenkanayama",
}

headers = {
    'Content-Type': 'application/json'
}

def run():
    time_sta = time.time()

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    # print(response.text)

    time_end = time.time()
    # 経過時間（秒）
    tim = time_end- time_sta
    print("経過時間（秒）：",tim)  # 大体4.5秒

if __name__ == '__main__':
    run()
