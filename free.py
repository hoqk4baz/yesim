import requests
from bs4 import BeautifulSoup
import random
import string
import sys
import os
import time
from concurrent.futures import ThreadPoolExecutor
import warnings

# ------- SSL hata ayıklaması için
# Yani konsoldan gizlemek için 
def handle_warning(message, category, filename, lineno, file=None, line=None):
    if category == requests.packages.urllib3.exceptions.InsecureRequestWarning:
        pass

warnings.showwarning = handle_warning

with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)



print("""
________              ______              
___  __ \_____ __________  /__ 
__  / / /  __ `/_  ___/_  //_/ 
_  /_/ // /_/ /_  /   _  ,<   
/_____/ \__,_/ /_/    /_/|_|""")
print("")

print("                        ENZA")

print("    Gemiler batti diye")

print("     Acirmi denizin cani..")
print("")



print("Created By TG: @dark_enza")
print("")



print("RedBull eSIM Sinirsiz")
print("")





device_id = '-'.join(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)) for _ in range(5))  # Rastgele bir deviceId oluştur
kullan = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))

name = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))  # Rastgele bir name oluştur (6 karakter)


print("[!]Dark Enzadan Izin Bekleniyor")
time.sleep(2)
i = requests.get("https://raw.githubusercontent.com/hoqk4baz/redbull/master/dark.json").json()
izin = i["dark"]
if izin == "izinli":
    print("[/]Izin Verildi\n")
else:
    print("[X]"+izin)
    raise SystemExit()

eposta = input("[@]Eposta: ")
sifre = input("[#]Sifre Gir: ")

url2 = "https://wndr.azurewebsites.net/api/v1/auth/login/email"
headers2 = {
    "X-Device-Model": "iPhone13,2",
    "Connection": "keep-alive",
    "X-Device-ID": device_id,
    "X-Device-Type": "iOS",
    "X-Accept-Version": "1.1",
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "X-App-Version": "1.3.0",
    "Host": "wndr.azurewebsites.net",
    "Accept-Language": "en",
    "User-Agent": "RBM%20data/84 CFNetwork/1390 Darwin/22.0.0",
    "Accept": "*/*"
}

data2 = {
    "email": eposta,
    "password": sifre
}

response2 = requests.post(url2, headers=headers2, json=data2)
sonuc2 = response2.json()
try:
    sonuc2 = response2.json()["accessToken"]
    print("[+]Token Cekildi")
except:
    print("[-]Token Cekilemedi Tekrar Dene")
    raise SystemExit()

headers3 = {
    "X-Device-Model": "iPhone13,2",
    "Connection": "keep-alive",
    "Authorization": "Bearer " + sonuc2,
    "X-Device-Type": "iOS",
    "X-Accept-Version": "1.1",
    "X-Device-ID": device_id,
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "X-App-Version": "1.3.0",
    "Host": "wndr.azurewebsites.net",
    "Accept-Language": "en",
    "User-Agent": "RBM%20data/84 CFNetwork/1390 Darwin/22.0.0",
    "Accept": "*/*"
}

def order_package():
    satin_al = "https://wndr.azurewebsites.net/api/v1/packages/order-free-package"
    satinal_data = {"packageId": "mDFiwArRhFsEJVhTEd_XU"}
    satinal = requests.post(satin_al, headers=headers3, json=satinal_data)
    sonucc = satinal.json()

    if sonucc == {}:
        print("\n[+]Paket Aktiflendi")
    else:
        print("[~]Paket Aktiflenmedi")
        raise SystemExit()

order_package()

while True:
    kontrol = requests.get("https://wndr.azurewebsites.net/api/v1/dashboard/active-packages", headers=headers3)
    kullanilan1 = kontrol.json()["packages"][0]["usedData"]
    kullanilan2 = kontrol.json()["packages"][0]["usedData"]

    if kullanilan1 == 1124:
        order_package()

    print("[*]"+str(kullanilan2)+"MB Kullandin")
    time.sleep(3)


	


