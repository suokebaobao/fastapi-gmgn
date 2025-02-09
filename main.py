# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import asyncio

from gmgnPage import gmgnPage
from gmgnCoins import getInfo
import asyncio
import telegram # python-telegram-bot
from telegram.ext import *

async def sendMsg():
    bot = telegram.Bot("8110770762:AAE8T64ms28K0WBJXBJIlh9hjI8zsT3Ai1c")
    async with bot:
        text = f"Hi John!\nHi John!"
        await bot.send_message(text=text, chat_id=6112223515)


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    gmgnPage()


