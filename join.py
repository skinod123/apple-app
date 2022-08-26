import time
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from app_config import API_ID, API_HASH
from telethon.errors.rpcerrorlist import FloodWaitError


chanels = ['TelethonChat', 'apple']


with TelegramClient('name', API_ID, API_HASH) as client:
    for chanel in chanels:
        try:
            client(JoinChannelRequest(chanel))
        except FloodWaitError as fwe:
            print(fwe)
            time.sleep(fwe.seconds+20)
        except Exception as e:
            print(e)

