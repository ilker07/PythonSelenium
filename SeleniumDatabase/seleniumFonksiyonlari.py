


from  selenium import webdriver
import time




def filmIsmi():
    return browser.find_element_by_css_selector("h1.left")  # Filmin ismini aldık.
def filmBilgi():
    return browser.find_elements_by_css_selector(".info-group")  # Film bilgilerini aldıkTür,Yapım vs.




film_linkleri=[]

browser=webdriver.Chrome(executable_path=r"C:\Users\İlker\Desktop\chromedriver.exe")

url="https://www.sinemalar.com/kullanici/ilkeraykut7/listeleri/9234/2013?page=6"

browser.get(url)



time.sleep(3)

filmler=browser.find_elements_by_css_selector('a.user-list-size.relative.shadow') #a tag ı içindeki user-list-size.relative.shadow classı.


for film in filmler:

  film_linkleri.append(film.get_attribute('href'))  #Sayfadaki Linkleri aldık.





