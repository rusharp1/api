from lostark_api_token import *
import requests
import datetime
import time
from openpyxl import Workbook

def draw_excel(jewel_info_list):
  wb = Workbook()
  ws = wb.active
  ws.title = "로스트아크 7레벨 보석 가격 변화 추이"

  # 헤더 추가
  ws.append(["", "번호", "시간", "보석 타입", "가격", "클래스명", "스킬명"])

  # 보석 정보 추가
  for i, value in enumerate(jewel_info_list):
    value = ["", i+1]+value
    ws.append(value)

  # 열 범위 설정 (B~G)
  columns = [chr(i) for i in range(ord('B'), ord('H'))]
  lenth = len(jewel_info_list) + 1

  # MAX 값 수식 입력
  max = ([f"=INDEX({col}2:{col}{lenth}, MATCH(MAX(D2:D{lenth}),D2:D{lenth}, 0))"\
          for col in columns])
  max.insert(0, "max")
  ws.append(max)
  
  # MIN 값 수식 입력.
  min = ([f"=INDEX({col}2:{col}{lenth}, MATCH(MIN(D2:D{lenth}),D2:D{lenth}, 0))"\
          for col in columns])
  min.insert(0, "min")
  ws.append(min)

  # 엑셀 파일 저장
  wb.save("lostark_jewel.xlsx")
  
def fetch_jewel_data(url, headers, Body):
  # post response값 받아옴.
  response = requests.post(url, headers=headers, data= Body)
  # 200 코드 받아오면(정상 작동)
  if(response.status_code == 200):
    jsonData = response.json()
    if jsonData["Items"]:
      # 현재 시간, 보석 타입, 클래스명, 스킬명, 최저 가격
      now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
      price = jsonData["Items"][0]["AuctionInfo"]["BuyPrice"]
      jtype = jsonData["Items"][0]["Name"]
      class_name = jsonData["Items"][0]["Options"][0]["ClassName"]
      skill_name = jsonData["Items"][0]["Options"][0]["OptionName"]

      # 리스트에 값 추가.
      return([now, price, jtype, class_name, skill_name])
    else:
      print("검색 결과가 없습니다.")
      return None
  else:
    print("Error Code:" + response.status_code)
    return None
   
def main():
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
  jewel_info_list = []

  # 60회 반복 (한 시간 동안 1분 간격)
  for i in range(60):
    # 검색 값을 받아서 jewel_data 에 저장하기
    jewel_data = fetch_jewel_data(url, headers, Body)
    if jewel_data:
       jewel_info_list.append(jewel_data)

    # 60초 대기하기 (1분단위)
    time.sleep(60)

  draw_excel(jewel_info_list)

# 코드가 직접 실행될 때만 실행됨
if __name__ == "__main__":
    main()