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

REG = r'tcp://[^\"]*'
TGTOKEN = ''
CHATID = ''


def telegram_bot_sendtext(bot_message): 
    try:
        send_text = f'https://api.telegram.org/bot{TGTOKEN}/sendMessage?chat_id={CHATID}&parse_mode=Markdown&text={bot_message}'
        response = requests.get(send_text)
        return response.json()
    except Exception as conerr:
        print(f'[-] Connection aborted to Telegram API. Error: {conerr}')


################# MAIN EXECUTION #################
if not TGTOKEN or not CHATID:
    print("[-] Please insert a valid Telegram Bot Token or ChatID and rerun the program!")
    sys.exit(1)
else:
    print(f'[+] Telegram Info found! -> {TGTOKEN}')

data = ''
respstat = ''

try:
    ngresp = requests.get('http://127.0.0.1:4040/api/tunnels')
    respstat = ngresp.status_code
    data = ngresp.text
except Exception as conerr:
    print(f'[-] Connection aborted to Ngrok API. Error: {conerr}')

endpoint = re.findall(REG, data)
if len(endpoint) == 0:
    message = f'Failed to retrieve your endpoint, check ngrok configuration.\nthanks for using BlackKaliLoader!'
else:
    message = f"Your Endpoint is {endpoint} , thanks for using BlackKaliLoader!"

tgresp = telegram_bot_sendtext(str(message))
if tgresp['ok'] is True:
    print("[+] Telegram message sent!")
else:
    print("[-] Error sending telegram message!")
