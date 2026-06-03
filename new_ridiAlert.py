import sys
import discord
import asyncio
from discord.ext import commands, tasks
import datetime
import new_ridiRequest as req
import new_ridiInfo as rdinfo


# 봇의 설정 및 봇 객체 생성
prefix = "!"  # 봇의 명령어 접두사
bot_intents = discord.Intents.default()
bot = commands.Bot(command_prefix=prefix, intents=bot_intents)

TOKEN = rdinfo.token
CHANNEL_ID = rdinfo.channelID 


#bot 실행 함수
def run_bot():
    bot.run(TOKEN)

@bot.event
async def on_ready():
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}    INFO    {bot.user.name}: 봇이 로그인하였습니다")
    time_sender.start()  
    
#@tasks.loop(seconds=5, count=1)  # 테스트용
@tasks.loop(minutes=29, count=3) # 실제 run
async def time_sender():
    channel = bot.get_channel(CHANNEL_ID)
    now = datetime.datetime.now()
    # 사이트 구조 변경 감지 시: 경고 발송 후 종료 (정상 알림 생략)
    if not req.structure_ok:
        await channel.send(
            f"[구조 변경 감지] 기상청 페이지 파싱에 실패했습니다.\n"
            f"시각: {now.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"사유: {req.structure_reason}\n"
            f"→ new_ridiRequest.py의 파싱 로직 점검이 필요합니다.\n"
            f"-----------------------------------------"
        )
        print(f"{now.strftime('%Y-%m-%d %H:%M:%S')}    WARNING    {bot.user.name}: 구조 변경 감지 — {req.structure_reason}")
        return

    if req.isRain == True:
        await channel.send(f"[discord] 현재 시간은 {now.strftime('%Y-%m-%d %H:%M:%S')}입니다.\n  {rdinfo.param_date[:-3]}엔 비가 왔어요 \n [비 포인트 받으러 가기](https://ridibooks.com/)\n -----------------------------------------")
        print(f"{now.strftime('%Y-%m-%d %H:%M:%S')}    INFO    {bot.user.name}: 비포 알림 발송 완료")
    else:
        await channel.send(f"[discord] 현재 시간은 {now.strftime('%Y-%m-%d %H:%M:%S')}입니다. \n {rdinfo.param_date[:-3]}엔 비가 오지 않았어요.\n -----------------------------------------")
        print(f"{now.strftime('%Y-%m-%d %H:%M:%S')}    INFO    {bot.user.name}: 알림 발송 완료")


# 루프 끝나면 bot.close 시키는 함수
@time_sender.after_loop
async def after_time_sender():
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}    INFO    time_sender 루프 종료\n-----------------------------------------")
    await bot.close()



# 봇을 실행
run_bot()
