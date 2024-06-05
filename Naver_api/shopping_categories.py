from naver_api_token import *
import requests
import json

# 그룹으로 묶은 검색어에 대한 네이버 통합검색에서 검색 추이 데이터를 반환.
url = "https://openapi.naver.com/v1/datalab/shopping/categories"

# 헤더 설정
headers = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret,
    "Content-Type": "application/json"
}

# 요청 본문 데이터 설정
body = {
    "startDate": "2024-01-01",
    "endDate": "2024-06-03",
    "timeUnit": "month",
    "category": [
        {"name": "노트북", "param": ["50000151"]},
        {"name": "PC", "param": ["50000089"]}
    ],
    "device": "pc",
    "gender": "f",
    "ages": ["20", "30"]
}

# POST 요청 보내기
# json.dumps(body) 는 body dictionary를 JSON 형식의 문자열로 변환함.
response = requests.post(url, headers=headers, data=json.dumps(body))

# 응답 출력
print("Status Code:", response.status_code)
print("Response Body:", response.json())

if(response.status_code==200):
    response_body = response.json()
    print(response_body)
else:
    print("Error Code:" + response.status_code)