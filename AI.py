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
    veritabani = veritabani_yukle()
    while True :
          soru =input("Siz:")

          if soru =='Çık':
              break
          gelen_sonuc = yakin_sonuc_bul(soru,[sorucevaplar["soru"]for sorucevaplar in veritabani["sorular"]])
          if gelen_sonuc:
               verilecek_cevap =cevabini_bul(gelen_sonuc,veritabani)
               print(f"Bot:{verilecek_cevap}")

          else :
               print("Bot:Bunu nasıl cevaplayacağımı bilmiyorum.Öğretir misiniz?")
               yeni_cevap =input("Öğretmek için yazabilir veya geç diyebilirsiniz.")

               if yeni_cevap !='geç':
                    veritabani["sorular"].append({
                         "soru":soru,
                         "cevap":yeni_cevap
                    })
                    veritabaina_yaz(veritabani)
                    print("Bot:Teşekkürler ,sayenizde yeni bir şey öğrendim.")
if __name__ =='__main__':
        chat_bot()        