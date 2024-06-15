import requests
from lostark_api_token import *

def get_character_info(characterName):
    # 계정의 모든 캐릭터 정보
    link = f"/characters/{characterName}/siblings"
    headers = {
        'accept': 'application/json',
        'authorization': authorization_key
    }

    response = requests.get(lostark_url + link, headers=headers)
    #오류 발생 시 예외를 던짐
    response.raise_for_status()
    return response.json()

def get_serverName(characters):
    # 서버이름 목록 가져온 뒤 중복제거
    ServerName_list = [character['ServerName'] for character in characters]
    return list(set(ServerName_list))

def characters_by_server(characters, ServerName_list):
    # 서버 별 캐릭터 목록으로 정리하기
    # {서버명 : 캐릭터 목록 list}
    char_info_list = {}
    for servername in ServerName_list:
        char_info_list[servername] = \
            [char for char in characters if char['ServerName'] == servername]
    return char_info_list

def get_profile_images(character):
    # 캐릭터 이미지 가져오기 (API GET)
    link = f"/armories/characters/{character['CharacterName']}/profiles"
    headers = {
        'accept': 'application/json',
        'authorization': authorization_key
    }
    response = requests.get(lostark_url + link, headers=headers)
    
    # 캐릭터 이미지 중 'CharacterImage'에 해댕하는 내용만 가져옴
    return response.json()['CharacterImage']

def display_characters(char_info_list):
    for key, value in char_info_list.items():
        print("==================================================")
        print("서버명 : {!r:10s} 캐릭터 수 : {}".format(key.replace("'", ""), len(value)))
        print("==================================================")
        for character in value:
            
            # 캐릭터 이미지 가져오기
            profile_image = get_profile_images(character)

            # 캐릭터 정보 출력
            print("캐릭터 프로필 : {}".format(profile_image))
            print("캐릭터명      : {} ".format(character['CharacterName']))
            print("캐릭터 레벨   : {} ".format(character['CharacterLevel']))
            print("클래스        : {} ".format(character['CharacterClassName']))
            print("아이템 레벨   : {} ".format(character['ItemMaxLevel']))
            print()


def main():
    # 로스트아크
    characterName = input("캐릭터 이름을 입력해 주세요 : ")

    # 캐릭터 이름별로 기본 능력치 요약을 반환.
    # link = f"armories/characters/{characterName}/profiles"

    # 캐릭터 전체 정보 가져오기
    characters = get_character_info(characterName)
    # 캐릭터 서버 정보 가져오기
    ServerName_list = get_serverName(characters)
    # 포함된 서버 별 캐릭터 목록 가져오기
    char_info_list = characters_by_server(characters, ServerName_list)
    # 서버이름 별 캐릭터 출력하기
    display_characters(char_info_list)

if __name__== "__main__":
   main()