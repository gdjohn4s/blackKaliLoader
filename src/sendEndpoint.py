#!/usr/bin/env python3

# Project Name: BlackKaliLoader
# Module Name: sendEndpoint.py
# Author: gdjohn4s
# Email: john4s@protonmail.ch
# Version: 1.0.0

# LICENSE:
# This program is free software: you can redistribute it and/or modify it under the terms of the 
# GNU General Public License as published by the Free Software Foundation, either version 3 of the 
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU General Public License for more details.

import requests
import re
import sys
from urllib3 import exceptions as exp

REG = r'tcp://[^\"]*'
TGTOKEN = ''
CHATID = ''


def telegram_bot_sendtext(bot_message):
    """
    Send Telegram message with ngrok endpoint using Telegram Api
    """
    try:
        send_text = f'https://api.telegram.org/bot{TGTOKEN}/sendMessage?chat_id={CHATID}&parse_mode=Markdown&text={bot_message}'
        response = requests.get(send_text)
        return response.json()
    except Exception as conerr:
        print(f'[-] Connection aborted to Telegram API. Error: {conerr}')


def getChatId():
    """
    Trying to get ChatID using Telegram API
    """
    updates = f'https://api.telegram.org/bot{TGTOKEN}/getUpdates'
    req = requests.get(updates)
    res = req.json()
    if not res['result']:
        print('[+] Can\'t get ChatID, insert manually!')
        return None
    else:
        print('[+] ChatId gained')
        return res['result'][0]['my_chat_member']['chat']['id']


################# MAIN EXECUTION #################
# If TelegramToken not set, it will exit
if not TGTOKEN:
    print("[-] Please insert a valid Telegram Bot Token and rerun the program!")
    sys.exit(1)
else:
    print('[+] Telegram Info found!')

# If ChatID not set, it will try to get using telegram api by setting your telegram bot token
if not CHATID:
    print('[-] Hey don\'t you set ChatID in this code? Ok.. I\'ll Trying to get it from API..')
    CHATID = getChatId()
else:
    print('[-] Error getting chatID from Telegram Api! Check your configuration')
    sys.exit(1)

data = ''
respstat = ''

# Here we got ngserver information by sending a get request to our ngrok session using ngrok api
# If not reachable trow general exception
try:
    ngresp = requests.get('http://127.0.0.1:4040/api/tunnels')
    respstat = ngresp.status_code
    data = ngresp.text
except Exception as conerr:
    print(f'[-] Connection aborted to Ngrok API. Error: {conerr}')

# Using a Regex we'll get the exact endpoint value from ngrok api response
endpoint = re.findall(REG, data)
if len(endpoint) == 0:
    message = f'Failed to retrieve your endpoint, check ngrok configuration.\nthanks for using BlackKaliLoader!'
else:
    message = f"Your Endpoint is {endpoint} , thanks for using BlackKaliLoader!"

# Then finally send telegram message!
# If 'ok' value from telegram json response is True then message sent otherwise False
tgresp = telegram_bot_sendtext(str(message))
if tgresp['ok'] is True:
    print("[+] Telegram message sent!")
else:
    print("[-] Error sending telegram message!")
