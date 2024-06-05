from naver_api_token import *
import requests
import pprint

url = "https://openapi.naver.com/v1/search//local.json"

# 헤더 설정
headers = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret,
}
# 파라미터값 지정
params = {
    "query": "seoul"
}
# requests.get을 통해 GET 요청받음
response = requests.get(url, headers=headers, params=params)

# 코드번호가 200이면 결과값 출력.
# 아니면 에러코드번호 출력
if(response.status_code==200):
    response_body = response.json()
    pprint.pprint(response_body)
else:
    print("Error Code:" + response.status_code)