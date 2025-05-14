import json
from difflib import get_close_matches as yakin_sonuclari_getir
def veritabani_yukle():
    with open('C:\\Users\\SENAY\\Desktop\\PythonAI\\veritabani.json','r') as dosya:
        return json.load(dosya)
def veritabaina_yaz(veriler):    
    
    with open('C:\\Users\\SENAY\\Desktop\\PythonAI\\veritabani.json','w') as dosya:
        json.dump(veriler,dosya,indent=2)