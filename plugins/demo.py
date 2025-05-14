import asyncio
from nonebot import on_message
from nonebot.rule import to_me

weather = on_message(rule=to_me(), priority=10, block=True)

@weather.handle()
async def handle_function():
    await weather.send("等待中...")
    await asyncio.sleep(10)
    await weather.finish("天气是晴朗！")