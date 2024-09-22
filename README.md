<img src="https://capsule-render.vercel.app/api?type=waving&amp;color=BDBDC8&amp;height=150&amp;section=header">

# api

> python을 사용하여 api의 데이터를 받고, 응용.

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Frusharp1%2Fapi&count_bg=%233B3B3B&title_bg=%23B178BE&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

## 1\. lostark\_api

### 1\. 프로젝트 목록

#### 1. lostark charecter get.py
1. 프로젝트 개요 (Introduction)
    * 이 프로젝트는 **로스트아크**에서 특정 캐릭터명을 입력하면, 해당 계정 내 모든 캐릭터의 정보를 출력하는 Python 스크립트입니다. 이를 통해 계정 내의 캐릭터들의 이름, 레벨, 클래스, 아이템 레벨 등의 세부 정보를 확인할 수 있습니다.
2. 기능 설명 (Features)
    * 계정 내 모든 캐릭터의 정보를 조회
    * 캐릭터가 속한 서버별로 정리된 목록 제공
    * 각 캐릭터의 프로필 이미지, 레벨, 클래스, 아이템 레벨 정보 출력
3. 명령어 실행 예시
    <details>
      <summary>명령어 실행 예시 보기/접기</summary>
    - 서버명 별로 캐릭터 개수가 출력되며, 프로필 조회가 되는 경우, 프로필을 링크로 제공
        <img src = "https://github.com/user-attachments/assets/799e1620-e08d-42e9-8cc4-fe79a4c1250f" alt = "명령어 실행 예시">
    </br>
      - 캐릭터 프로필 이미지를 찾을 수 없거나, 불러오지 않는 경우 링크가 노출되지 않음
         <img src = "https://github.com/user-attachments/assets/bcb8685e-9d8d-4384-90ae-1a60ca18252a" alt = "명령어 실행 예시">
    </details>
#### 2. lostark auction jewel plt.py
1. 프로젝트 개요 (Introduction)
    * 이 프로젝트는 **로스트아크**의 7레벨 보석 가격 변화를 실시간으로 모니터링하고, 가격 변화를 시각화하는 Python 스크립트입니다. 특정 API를 호출하여 보석의 가격 데이터를 수집하고, 이를 그래프로 표현함으로써 사용자가 가격 변동 추이를 쉽게 이해할 수 있도록 도와줍니다.
2. 기능 설명 (Features)
    * 로스트아크 API를 통해 3티어의 7레벨 보석의 최저 가격 데이터를 실시간으로 수집합니다.
    * 수집된 가격 데이터를 Matplotlib을 사용하여 그래프로 시각화합니다.
    * 1분 간격으로 가격을 기록하여, 시간에 따른 가격 변화를 보여줍니다.
    * 각 데이터 포인트에 가격 정보를 주석으로 표시하여 가독성을 높입니다.
3. 명령어 실행 예시
    <details>
      <summary>명령어 실행 예시 보기/접기</summary>
        <img src = "https://github.com/user-attachments/assets/96ca86fa-9123-431d-b29c-f3263234364a" alt = "명령어 실행 예시">
    </details>
#### 3. lostark auction jewel excel.py
1. 프로젝트 개요 (Introduction)
    * 이 프로젝트는 **로스트아크**의 7레벨 보석 가격 변화를 실시간으로 모니터링하고, 가격 변화를 시각화하는 Python 스크립트입니다. 특정 API를 호출하여 보석의 가격 데이터를 수집하고, 이를 엑셀 파일로 저장하여 사용자가 가격 변동 추이를 쉽게 분석할 수 있도록 합니다.
2. 기능 설명 (Features)
    * 로스트아크 API를 통해 3티어의 7레벨 보석의 최저 가격 데이터를 실시간으로 수집합니다.
    * 수집된 가격 데이터를 OpenPyXL을 사용하여 엑셀 파일에 기록합니다.
    * 수집된 가격 데이터의 최대값과 최소값을 자동으로 계산하여 엑셀 파일에 기록합니다.
    * 1분 간격으로 가격을 기록하여, 시간에 따른 가격 변화를 보여줍니다.
3. 명령어 실행 예시
      <details>
         <summary>명령어 실행 예시 보기/접기</summary>
            <a href="https://github.com/user-attachments/files/17088528/lostark_jewel_test.xlsx" target="_blank">
          lostark_jewel_test.xlsx 파일 다운로드
        </a>
          </details>


### 2\. 사전 요구사항 \(Prerequisites\)

* Python 3.x 설치
* `requests` 라이브러리 설치
* `matplotlib` 라이브러리 설치
* `openpyxl` 라이브러리 설치

### 3. 사용한 API [출처](https://developer-lostark.game.onstove.com/)
1.  lostark charecter get.py
    * [https://developer-lostark.game.onstove.com/armories/characters/"CharacterName"/profiles](https://developer-lostark.game.onstove.com/armories/characters/%22CharacterName%22/profiles)
    * [https://developer-lostark.game.onstove.com/characters/"CharacterName"/siblings](https://developer-lostark.game.onstove.com/characters/%22CharacterName%22/siblings)
2. lostark auction jewel plt.py
    * [https://developer-lostark.game.onstove.com/auctions/items](https://developer-lostark.game.onstove.com/auctions/items)

3. lostark auction jewel excel.py
    * [https://developer-lostark.game.onstove.com/auctions/items](https://developer-lostark.game.onstove.com/auctions/items)

### 4\. 참고사항 \(Notes\)

* lostark\_api\_token.py 파일에 API 인증 키가 필요합니다. 로스트아크 개발자 페이지에서 발급받은 authorization\_key를 설정해주세요.
* lostark charecter get.py 에서 네트워크 오류 또는 데이터 누락 시 예외 처리가 발생할 수 있으며, 이러한 경우 "값을 받을 수 없습니다"가 출력됩니다.
* lostark\_auction\_jewel \* .py 에서 가격 데이터 수집은 1시간동안 진행되며, 실행 중 API 호출이 제한될 수 있으므로 주의가 필요합니다.

### 5\. 설치 방법 \(Installation\)

1. 프로젝트를 로컬에 클론합니다.

    ```
    git clone -b master https://github.com/rusharp1/api.git
    ```
2. 해당 프로젝트 위치로 이동합니다.

    ```
    cd ./api/lostark_api
    ```
3. 원하는 프로젝트를 실행합니다.

    ```
    파일명.py
    ```
## 3\. Naver API
 
### 1\. 프로젝트 목록

#### 1. search_local.py
1. 프로젝트 개요 (Introduction)
    * 이 프로젝트는 네이버의 오픈 API를 활용하여 지역 정보를 검색하는 Python 스크립트입니다. 사용자는 네이버 API의 로컬 검색 기능을 통해 특정 지역을 검색할 수 있으며, 요청에 대한 응답을 JSON 형식으로 받아 이를 출력합니다. 이를 통해 원하는 지역 정보를 쉽게 조회하고 활용할 수 있습니다. 기본적인 API 와 python 을 사용하기 위해 연습한 프로젝트 입니다.
2. 기능 설명 (Features)
    * 네이버 지역 서비스에 등록된 업체 및 기관중 서울 지역의 검색 결과를 pprint를 사용하여 가독성을 높여 출력
3. 명령어 실행 예시
      <details>
         <summary>명령어 실행 예시 보기/접기</summary>
            <img src = "https://github.com/user-attachments/assets/a7e638fd-fc5d-4a6e-8690-63aeebd68a7d" alt = "명령어 실행 예시">
          </details>
#### 2. shopping_categories.py
1. 프로젝트 개요 (Introduction)
    * 이 프로젝트는 네이버 쇼핑인사이트 API를 활용하여 특정 카테고리의 쇼핑 트렌드를 조회하는 프로그램입니다. 사용자는 지정한 기간 동안의 카테고리별 트렌드 데이터를 조회할 수 있습니다. 이 프로젝트에서는 '노트북'과 'PC'에 대한 검색 트렌드를 조회하고, 결과를 출력하는 기능을 제공합니다.
2. 기능 설명 (Features)
    * 네이버 쇼핑인사이트 API를 사용해 특정 카테고리(노트북, PC)의 월별 쇼핑 트렌드 데이터를 조회.
    * 조회된 결과를 JSON 형식으로 받아 가독성을 높이기 위해 pprint를 사용하여 출력.
3. 명령어 실행 예시
      <details>
         <summary>명령어 실행 예시 보기/접기</summary>
            <img src = "https://github.com/user-attachments/assets/729568aa-9a2e-4fe6-953a-956c5f9df912" alt = "명령어 실행 예시">
          </details>
### 2\. 사전 요구사항 \(Prerequisites\)

* Python 3.x 설치
* `requests` 라이브러리
* `pprint `모듈 (Python 내장 모듈)


### 3. 사용한 API [출처](https://developers.naver.com/docs/common/openapiguide/apilist.md#%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EB%B0%A9%EC%8B%9D-%EC%98%A4%ED%94%88-api)
1.  search_local.py
    * https://openapi.naver.com/v1/search//local.json
2. shopping_categories.py
    * https://openapi.naver.com/v1/datalab/shopping/categories

### 4\. 참고사항 \(Notes\)
* naver_api_token.py 파일에 API 인증 키가 필요합니다. 네이버 개발자 페이지에서 발급받은 client_id 와 client_secret 을 설정해주세요.
### 5\. 설치 방법 \(Installation\)

1. 프로젝트를 로컬에 클론합니다.

    ```
    git clone -b master https://github.com/rusharp1/api.git
    ```
2. 해당 프로젝트 위치로 이동합니다.

    ```
    cd ./api/Naver_api
    ```
3. 원하는 프로젝트를 실행합니다.

    ```
    파일명.py
    ```
## 4. LICENSE 
이 프로젝트는 [MIT License](LICENSE) 에 따라 라이선스가 부여됩니다.
<img src="https://capsule-render.vercel.app/api?type=waving&amp;color=BDBDC8&amp;height=150&amp;section=footer">
