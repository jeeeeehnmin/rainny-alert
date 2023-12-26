import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
import datetime
import ridiInfo as rdinfo

url = rdinfo.url

# 웹페이지 내용 가져오기
response = requests.get(url)
html = response.text
isRain = ""

### 전체에서 http status 체크해서 200이면 실행시키기

if response.status_code == 200:
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find_all('table')[1]

    # 테이블의 각 행을 반복하면서 데이터 추출
    row_counter = 0
    color_attr =""
    list_isRain = list() 
    for row in table.find_all('tr'):
        if row_counter >= 8:
            break
        columns = row.find_all('td')
        # print(columns)
        if len(columns) >= 2 :
            time = columns[0].text.strip()  # 시간 데이터 추출
            colors = columns[1].find_all('font')
            for col in colors:
                color_attr = col["color"]
                list_isRain.append(color_attr)
        
            print(f'시간: {time}, 강수: {color_attr}')
            row_counter += 1
    #print(list_isRain)

    # blue가 포함되면 success, none 표시하기
    if 'blue' in list_isRain:
        isRain = True
    else:
        isRain = False
    print(isRain)

else:
    isRain = 'Error'
    print(f'HTTP 요청이 실패하였습니다. 상태 코드: {response.status_code}')
