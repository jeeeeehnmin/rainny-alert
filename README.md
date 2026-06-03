# 프로젝트 개요
평일 오전 10시 ~ 오후 4시 사이에 선릉역에 비가 오면 알려주는 디스코드 챗봇

created by @jeeeeehnmin
& chatGPT의 도움 조금


### 크롤링하는 웹페이지 정보
- 크롤링한 웹페이지의 날씨 데이터는 table 형식으로 되어 있으며 시간(분 단위)별로 값이 노출되고 있음
- 데이터 행은 첫 번째 셀이 `HH:MM` 형식이며, 컬럼 순서는 다음과 같음
    - `시:분[0]` | `1시간강수(mm)[1]` | `일강수(mm)[2]` | `기온[3]` | ...
- 비가 오는지 여부는 `1시간강수(mm)` 컬럼의 숫자 값으로 판단함
    - 값이 0보다 크면, 비가 옴
    - 값이 0이거나 비어 있으면, 비가 오지 않음
- (구버전) 과거에는 강수 셀의 css color(red=비 안옴 / blue=비옴) 또는 `유/무` 텍스트로 구분했으나, 사이트 구조 변경으로 현재는 숫자(mm) 방식으로 판단함

- 혹시나 이 소스를 사용하려는 사람이 있다면 new_ridiRequest.py 파일을 크롤링하려는 웹페이지의 구조에 맞게 수정해야 함

### 사이트 구조 변경 감지
- 기상청 페이지 구조가 바뀌어 파싱이 깨지는 경우를 자동으로 감지함
- 별도 실행 없이 기존 배치 주기(크롤링) 안에서 함께 판단하며, 감지 시 디스코드 채널 메시지 + 로그로 알림
- 감지 기준
    - HTTP 200이지만 데이터 행(`HH:MM`)을 하나도 찾지 못함 → 테이블 구조 변경 또는 데이터가 JS/AJAX로 로딩되는 것으로 추정
    - 데이터 행은 있으나 `1시간강수` 컬럼을 찾지 못함 → 컬럼 구성 변경 추정
- 감지되면 평소 비/비안옴 알림 대신 `[구조 변경 감지]` 경고 메시지를 발송함 (강수 판정값을 신뢰할 수 없기 때문)



# 설정
## 버전 정보
- UBUNTU 22.04.3 LTS
- 파이썬 3.10.12

## 프로젝트 초기 설정
```
pip install -r requirements.txt
```
- 윈도우인 경우, 패키지 이름이 안맞아서 오류날 수 있음, 이 때는 개별 설치 진행


## 디렉토리 구조
```
rainny-alert/
├─── alertLog/             # 로그 저장 폴더 / .gitignore에 포함되어 있음
├─── .gitignore
├─── README.md
├─── requirements.txt      # 파이썬 패키지 파일 설치
├─── new_ridiAlert.py      # discord에 메시지 전송 수행 + 구조 변경 감지 시 경고 발송
├─── new_ridiInfo.py       # token, channelID, 크롤링할 웹페이지 URL / .gitignore에 포함되어 있음
└─── new_ridiRequest.py    # BeautifulSoup으로 HTML 파싱·데이터 추출 + 사이트 구조 변경 감지


```



# 디스코드 챗봇 설정은 self
``` 2023.12.26 작성 기준```

1. Applications(https://wwww.discord.com/developers/applications) 접속  
1-1. 우상단 New Application 버튼 선택  
1-2. 이름 지정 & 약관 동의   

2. Applications 하단 my Applications에서 생성된 application 선택  

3. 좌측 Bot 메뉴 선택 후 token 정보 복사  --> ridiInfo.py / token  
- 1회만 발급되고 잃어버리는 경우, 재발급해서 사용해야 하니 주의  
3-1. ``` MESSAGE CONTENT INTENT``` 활성화  
3-2. Save changes 버튼 선택  

4. 좌측 OAuth2 메뉴 선택 후 하위의 URL Generator 메뉴 선택  
4-1. SCOPES에서 ```bot``` 활성화  
4-2. BOT PERMISSION에서 TEXT PERMISSIONS > ```Send Messages``` 활성화  
4-3. 생성된 GENERATED URL 확인  
4-4. 생성된 GENERATED URL 실행  

5. IMPORT할 서버 선택  
5-1. 서버 내 실행시킬 채널 선택  
5-2. 해당 채널 이름 위에 마우스를 두고 우클릭 실행  
5-3. 채널 ID 복사하기 실행 --> ridiInfo.py / channelID  
