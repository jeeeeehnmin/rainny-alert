#!/bin/sh
echo "ridiAlert.py 스크립트가 실행되었습니다." | logger

python3 /home/jhmin/Project/ridi/ridiAlert.py >> /home/jhmin/Project/ridi/alertLog/log_$(date +\%Y\%m\%d).log