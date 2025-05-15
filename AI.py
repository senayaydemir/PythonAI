import json
from difflib import get_close_matches as yakin_sonuclari_getir
def veritabani_yukle():
    with open('C:\\Users\\SENAY\\Desktop\\PythonAI\\veritabani.json','r') as dosya:
        return json.load(dosya)
def veritabaina_yaz(veriler):    
    
    with open('C:\\Users\\SENAY\\Desktop\\PythonAI\\veritabani.json','w') as dosya:
        json.dump(veriler,dosya,indent=2)

def yakin_sonuc_bul(soru,sorular):
    eslesen=yakin_sonuclari_getir(soru,sorular,n=1,cutoff=0.6)
    return eslesen[0] if eslesen else None

def cevabini_bul(soru,veritabani):
    for sorucevaplar in veritabani["sorular"]:
        if sorucevaplar["soru"]==soru:
            return sorucevaplar["cevap"]
        return None

def chat_bot():
 veritabani_yukle()
while True :
    soru =input("Siz:")

    if soru =='Çık':
        break

if __name__ =='__main__':
        chat_bot()        