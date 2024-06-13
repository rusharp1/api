import requests
import json
import pprint
from lostark_api_token import authorization_key

# 로스트아크
url =  "https://developer-lostark.game.onstove.com/"
characterName = input("캐릭터 이름을 입력해 주세요 : ")

# 캐릭터 이름별로 기본 능력치 요약을 반환합니다.
# link = f"armories/characters/{characterName}/profiles"

# 계정의 모든 캐릭터 정보
link = f"characters/{characterName}/siblings"
headers = {
    'accept': 'application/json',
    'authorization': authorization_key
}

response = requests.get(url + link, headers=headers)
test = response.json()

# 서버이름 목록 가져온 뒤 중복제거
ServerName_list = []
for ServerName in test:
    ServerName_list.append(ServerName['ServerName'])

ServerName_list = list(set(ServerName_list))

# 서버 별 캐릭터 목록으로 정리하기
# {서버명 : 캐릭터 목록 list}
char_info_list = {}
for servername in ServerName_list:
    char_list = []
    for n in range(len(test)):
        if test[n]['ServerName'] == servername:
            char_list.append(test[n])
        char_info_list[servername]  = char_list


# 서버이름 별 캐릭터 출력하기
for key, value in char_info_list.items():
    print("==================================================")
    print("서버명 : {!r:10s} 캐릭터 수 : {}".format(key.replace("'", ""), len(value)))
    print("==================================================")
    for v in value:
        # 캐릭터 이미지 가져오기 (API GET)
        link = f"armories/characters/{v['CharacterName']}/profiles"
        headers = {
            'accept': 'application/json',
            'authorization': authorization_key
        }
        response = requests.get(url + link, headers=headers)
        char_img = response.json()
        
        # 캐릭터 정보 출력
        print("캐릭터      : {}".format(char_img['CharacterImage']))
        print("캐릭터명    : {} ".format(v['CharacterName']))
        print("캐릭터 레벨 : {} ".format(v['CharacterLevel']))
        print("클래스      : {} ".format(v['CharacterClassName']))
        print("아이템 레벨 : {} ".format(v['ItemMaxLevel']))
        print()


# link = f"armories/characters/{characterName}/profiles"

# 두레이
# url =  "https://api.dooray.com/"
# api_key = "dooray-api jwvixmghaqn2:8irV3QhvT5-ldxntlIx2Mw"
# link = "project/v1/projects"

# # 프로젝트 목록을 받아옴.
# headers = {
#     "Authorization" : "dooray-api jwvixmghaqn2:8irV3QhvT5-ldxntlIx2Mw",
#     "Content-Type" : "application/json"}

# params = {f
#     "name" : "jtest"
# }



