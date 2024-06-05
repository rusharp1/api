from naver_api_token import *
import requests

url = "https://openapi.naver.com/v1/search//local.json"

# 헤더 설정
headers = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret,
}
params = {
    "query": "seoul"
}
response = requests.get(url, headers=headers, params=params)

if(response.status_code==200):
    response_body = response.json()
    print(response_body)
else:
    print("Error Code:" + response.status_code)