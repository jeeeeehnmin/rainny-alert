import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
import datetime
import re
import new_ridiInfo as rdinfo


# 결과를 저장할 딕셔너리
tr_result = {}

# 데이터 행 판별용: 첫 셀이 'HH:MM' 형태인지 확인
time_pattern = re.compile(r'^\d{1,2}:\d{2}$')

# 구조 변경 감지용 상태값 (new_ridiAlert.py에서 참조)
structure_ok = True
structure_reason = ""

# 빈 값('', '.')은 0.0으로 처리
def to_float(v):
    try:
        return float(v)
    except (ValueError, TypeError):
        return 0.0

http_error = False    # HTTP 오류(일시 장애)와 구조 변경을 구분하기 위함
header_found = False  # '1시간강수' 컬럼 헤더 존재 여부

# 시간대에 따라 크롤링 및 결과 저장
for param_time in ['11', '12', '13', '14', '15', '16']:
    url = rdinfo.param_url + rdinfo.param_date + param_time + rdinfo.param_option

    # 웹페이지 내용 가져오기
    response = requests.get(url)
    html = response.text
    isRain = ""

    ### http status 체크해서 200이면 실행
    if response.status_code == 200:
        # BeautifulSoup을 사용하여 HTML 파싱
        soup = BeautifulSoup(html, 'html.parser')

        # '1시간강수' 컬럼명이 페이지에 존재하는지 확인 (구조 검증용)
        if '1시간강수' in html.replace(' ', '').replace('\n', ''):
            header_found = True

        # 데이터 행만 추출
        # 컬럼 순서: 시:분[0] | 1시간강수(mm)[1] | 일강수(mm)[2] | 기온[3] | ...
        for tr in soup.find_all('tr'):
            cells = [td.get_text(strip=True) for td in tr.find_all('td')]
            if cells and time_pattern.match(cells[0]):
                tr_result[cells[0]] = cells[1]  # cells[1] = 1시간강수(mm)

    else:
        http_error = True
        isRain = 'Error'
        print(f'HTTP 요청이 실패하였습니다. 상태 코드: {response.status_code}')


# ---- 구조 변경 감지 ----
if http_error:
    # HTTP 오류는 일시적 장애일 수 있으므로 구조 변경으로 보지 않음
    structure_ok = True
elif len(tr_result) == 0:
    structure_ok = False
    structure_reason = "HTTP 200이지만 데이터 행(HH:MM)을 찾지 못함 — 테이블 구조 변경 또는 데이터가 JS/AJAX로 로딩되는 것으로 추정"
elif not header_found:
    structure_ok = False
    structure_reason = "데이터 행은 있으나 '1시간강수' 컬럼을 찾지 못함 — 컬럼 구성 변경 추정 (강수 판정이 틀릴 수 있음)"

# ---- 비 판정 ----
isRainYN = any(to_float(value) > 0 for value in tr_result.values())
isRain = True if isRainYN else False

## 로그용
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(url)
print(isRain)
if not structure_ok:
    print(f'[STRUCTURE-CHANGE] {structure_reason}')
print('------------------------------------------')
print(dict(sorted(tr_result.items())))
print('------------------------------------------')