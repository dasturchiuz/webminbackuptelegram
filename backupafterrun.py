import requests
from datetime import date
import os
# Bugungi vaqtni olamiz webminda backupda ko'rsatilgan format asosida
todayPath = date.today().strftime("%d-%m-%y")

API_TOKEN="here goes your access token from BotFather"
TELEGRAM_SEND_DOCUMENT_URL = f"https://api.telegram.org/bot{API_TOKEN}/sendDocument"
TELEGRAM_SEND_MESSAGE_URL = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"

#telegram chat ids
CHAT_IDS = [
    49690***,
    49690***,    
]


full_path=f"/var/backups/mysql/{todayPath}"

if (os.path.isdir(full_path)):
    listDirFiles = os.listdir(full_path)
    if(len(listDirFiles)>0):
        for chat_id in CHAT_IDS:
            for fileB in listDirFiles:
                res = requests.post(url=TELEGRAM_SEND_DOCUMENT_URL, data={'chat_id': chat_id}, files={'document': open(f"{full_path}/"+str(fileB), 'rb')} )
                if(res.status_code==200):
                    print(fileB + " - successful send")
                else:
                    res = requests.post(url=TELEGRAM_SEND_MESSAGE_URL, data={'chat_id': chat_id, 'text':f"{fileB} yuborilmadi"})
