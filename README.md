<img src="https://capsule-render.vercel.app/api?type=waving&amp;color=BDBDC8&amp;height=150&amp;section=header">

# api

> python을 사용하여 api의 데이터를 받고, 응용.

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Frusharp1%2Fapi&count_bg=%233B3B3B&title_bg=%23B178BE&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

## 1\. lostark\_api

### 1\. 프로젝트 목록

1. lostark charecter get.py
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
2. lostark auction jewel plt.py
4. lostark auction jewel excel.py

### 2\. 사전 요구사항 \(Prerequisites\)

* Python 3.x 설치
* `requests` 라이브러리 설치

### 3\. 참고사항 \(Notes\)

* lostark\_api\_token.py 파일에 API 인증 키가 필요합니다. 로스트아크 개발자 페이지에서 발급받은 authorization\_key를 설정해주세요.
* 캐릭터 프로필 API 호출 시 네트워크 오류 또는 데이터 누락 시 예외 처리가 발생할 수 있으며, 이러한 경우 "값을 받을 수 없습니다"가 출력됩니다.

### 4\. 설치 방법 \(Installation\)

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

## 2.


## 3\. 사용한 API
1. lostark_api (출처 : https://developer-lostark.game.onstove.com/ )
     * lostark charecter get.py
         * https://developer-lostark.game.onstove.com/armories/characters/"CharacterName"/profiles 
         * https://developer-lostark.game.onstove.com/characters/"CharacterName"/siblings
     * lostark auction jewel plt.py
         * https://developer-lostark.game.onstove.com/auctions/items
     * lostark auction jewel excel.py 
         * https://developer-lostark.game.onstove.com/auctions/items
## 4. LICENSE 
이 프로젝트는 [MIT License](LICENSE) 에 따라 라이선스가 부여됩니다.
<img src="https://capsule-render.vercel.app/api?type=waving&amp;color=BDBDC8&amp;height=150&amp;section=footer">
