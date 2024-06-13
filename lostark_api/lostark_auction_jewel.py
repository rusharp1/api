import pprint
from lostark_api_token import *
import requests
import json
import datetime
import time
import matplotlib.pyplot as plt


def draw_graph(timestamps, prices):
  # 한글 사용을 위한 폰트 설정
  plt.rcParams['font.family'] = 'Malgun Gothic'
  # 그래프 다크모드로 지정.
  plt.style.use('dark_background')

  # 그래프 크기 지정. (가로 10인치, 세로 5인치)
  plt.figure(figsize=(10, 5))
  # x 축은 timestamps, y 축은 가격 리스트, 각 데이터 포인트를 o 로 표시함.
  plt.plot(timestamps, prices, marker='o')

  for i, price in enumerate(prices):
    # price = 표시할 데이터
    # (timestamps[i], prices[i]) = 주석을 추가할 데이터 포인트 위치
    # textcoords="offset points = 텍스트 위치를 데이터 포인트 좌표를 기준으로 설정함
    # (0, 10) = 주석 텍스트의 시작 위치 (포인트 기준, 인치의 1/72)
    # 텍스트 수평 정렬을 중앙으로, text 색상은 흰색
    plt.annotate(f'{price}', (timestamps[i], prices[i]),
                  textcoords="offset points", xytext=(0, 10), ha='center', color='white')
    
  # X 라벨을 time, Y 라벨을 Price로 지정함.
  plt.xlabel('Time')
  plt.ylabel('Price')

  # 그래프 타이틀 지정
  plt.title('7레벨 보석 가격 변화 추이')

  # x 라벨을 45도 각도로 변환 (글자가 겹치지 않도록 함)
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.show()

url = lostark_url + "/auctions/items"

# 3티어, 7레벨의 보석을 즉시구매가 오름차순으로 검색함.
Body = {
  "Sort": "BUY_PRICE",
  "CategoryCode": 210000,
  "ItemTier": 3,
  "ItemName": "7레벨",
  "PageNo": 0,
  "SortCondition": "ASC"
}
headers = {
    'authorization': authorization_key,
    # 'Content-Type': 'application/json'
}

timestamps = []
prices = []

# 한시간 기다리기
for i in range(60):
  # 최저값 검색하기.
  response = requests.post(url,headers=headers, data=Body)
  if(response.status_code == 200):
      jsonData = response.json()
      if jsonData["Items"]:
        # 현재 시간 / 최저 가격을 now, price 변수에 입력
        now = datetime.datetime.now()
        price = jsonData["Items"][0]["AuctionInfo"]["BuyPrice"]

        # 리스트에 값 추가.
        timestamps.append(now.strftime('%Y/%m/%d %H:%M:%S'))
        prices.append(price)
      else:
         print("검색 결과가 없습니다.")
  else:
      print("Error Code:" + response.status_code)

  # 59초 대기하기 (1분단위 유도)
  time.sleep(59)

# 리스트에 값 추가.
timestamps.append(now.strftime('%Y/%m/%d %H:%M:%S'))
prices.append(price)

draw_graph(timestamps, prices)



