# 프로젝트 개요
평일 오전 10시 ~ 오후 4시 사이에 선릉역에 비가 오면 알려주는 디스코드 챗봇

created by @jeeeeehnmin
& chatGPT의 도움 조금


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
├─── alertLog/       # .gitignore에 포함되어 있음
├─── .gitignore
├─── README.md
├─── requirement.txt # 파이썬 패키지 파일 설치
├─── ridiAlert.py    # discord에 메시지 전송 수행
├─── ridiAlert.sh    # ridiAlert.py 파일 실행 및 로그 설정
├─── ridiInfo.py     # token, channelID, 크롤링할 웹페이지 URL / .gitignore에 포함되어 있음
└─── ridiRequest.py  # BeautifulSoup을 사용해서 HTML 파싱 및 데이터 추출




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
