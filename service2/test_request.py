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
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    print(response.text)

if __name__ == '__main__':
    run()
