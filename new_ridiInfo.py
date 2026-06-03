import os
from datetime import date, timedelta
import datetime
from dotenv import load_dotenv

# .env 로드
load_dotenv()


###### 디스코드 관련 정보
token = os.getenv("DISCORD_TOKEN")

# channelID는 데이터 타입을 따지는 편 → 반드시 int로 변환
channelID = int(os.getenv("DISCORD_CHANNEL_ID"))


###### 크롤링할 웹페이지 URL
param_url='https://www.weather.go.kr/w/weather/land/aws-obs.do?db=MINDB_01M&tm='
param_date = date.today().strftime('%Y')+'.'+date.today().strftime('%m')+'.'+date.today().strftime('%d')+'%20'
param_option = '%3A00&stnId=400&sidoCode=asos&sort=&config='

#param_url='https://www.weather.go.kr/w/observation/land/aws-obs.do?db=MINDB_01M&tm='



# real URL

# 비 옴
# param_date = '2024.01.03%20'
# param_date = '2026.05.20%20'
# url = "https://www.weather.go.kr/w/observation/land/aws-obs.do?db=MINDB_01M&tm=2024.01.03%2009%3A00&stnId=400&sidoCode=asos&sort=&config="

# 비 안옴
# param_date = '2024.01.02%20'
# param_date = '2026.06.03%20'

# url = "https://www.weather.go.kr/w/observation/land/aws-obs.do?db=MINDB_01M&tm=2024.01.02%2009%3A00&stnId=400&sidoCode=asos&sort=&config="
# url_test = "https://www.weather.go.kr/w/observation/land/aws-obs.do?db=MINDB_01M&tm=2024.01.03%2008%3A00&stnId=400&sidoCode=asos&sort=&config="
# print(url_test)

# Test
# if url == url_test:
#     print(True)
# else:
#     print(False)



# url 업데이트 10.29
# as-is param_url='https://www.weather.go.kr/w/obs-climate/land/aws-obs.do?db=MINDB_01M&tm='
# to-be param_url='https://www.weather.go.kr/w/observation/land/aws-obs.do?db=MINDB_01M&tm='