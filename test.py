import time
import requests
import asyncio
import datetime

from telegram import Bot

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import subprocess

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

suspended = '🟣Vietnam is still closed'
opening = '🟡OPENING! OPENING! OPENING!'

api_telegram_TOKEN = '6336049187:AAFXnQH_YBMiaCDaKSZKpbZJN1D920vSRz0' #Bot New Zealand

async def send_telegram(text):
	chat_ids = ['-968596336'] #Group test

	# Lấy thời gian hiện tại
	now = datetime.datetime.now()
	date_str = now.strftime("%d/%m/%Y")
	time_str = now.strftime("%H:%M:%S")

	# Tạo nội dung tin nhắn với thời gian
	text_with_timestamp = f"{text}\n🟣{date_str} {time_str}"

	bot = Bot(token=api_telegram_TOKEN)
	for chat_id in chat_ids:
	    await bot.send_message(chat_id=chat_id, text=text_with_timestamp)

sleep(600)
asyncio.run(send_telegram(suspended))