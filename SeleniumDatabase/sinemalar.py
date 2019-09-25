


import veriler
import bilgiler
import time
import seleniumFonksiyonlari
import degiskenler



for i in range(0,10):

 yeni_url=seleniumFonksiyonlari.film_linkleri[i] #Her link için dolaşıyoruz.
 seleniumFonksiyonlari.browser.get(yeni_url)
 time.sleep(3)


 for eleman in seleniumFonksiyonlari.filmBilgi():

    seleniumFonksiyonlari.browser.find_element_by_css_selector(".label")

    if eleman.text.startswith("Vizyon Tarihi") or eleman.text.startswith("Orijinal İsmi") : #a=eleman.text.strip("Vizyon Tarihi")  Bu kod sadece tarihi almak için yazılır.
        continue
    if eleman.text.startswith("Tür"):
        degiskenler.tur_degeri=bilgiler.ortakIslemler(eleman.text,"Tür")
    if eleman.text.startswith("Yapımı"):
        degiskenler.yapim_degeri=bilgiler.ortakIslemler(eleman.text,"Yapımı")
    if eleman.text.startswith("Süre"):
        degiskenler.sure_degeri=bilgiler.ortakIslemler(eleman.text,"Süre")



 #süre yapım tür boş değilse kontrolü yap.Sonra nesneyi oluştur.
 sinema_nesnesi=veriler.veri(seleniumFonksiyonlari.filmIsmi().text,degiskenler.tur_degeri,degiskenler.yapim_degeri,degiskenler.sure_degeri)  #1.para film.ismi.text
 with open("C:/Users/İlker/Desktop/Sinemalar.txt", "a", encoding="UTF-8") as file:
     file.write(sinema_nesnesi.filmIsminiGoster()+"\n")
     file.write(sinema_nesnesi.turuGoster() + "\n")
     file.write(sinema_nesnesi.yapimiGoster() + "\n")
     file.write(sinema_nesnesi.sureyiGoster() + "\n")


seleniumFonksiyonlari.browser.close()

