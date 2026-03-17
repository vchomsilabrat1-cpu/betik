from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
#------------------------------------
options = Options()
options.add_argument("--headless")
service = Service(r"C:\Users\Anvar\msedgedriver.exe")
driver = webdriver.Edge(service=service, options=options)
url = 'https://www.milligazete.com.tr/arsiv'
#-----------------------------------------------------------------------------------------------------------------------
def kategori(urr):
    driver.get(urr)
    htmll = driver.page_source
    soupp = BeautifulSoup(htmll, 'html.parser')
    kategorii=soupp.find("li",{"class":"breadcrumb-item active fw-bold"}).find("a").get_text()
    return kategorii
#------------------------------------
def tarih(urr):
    driver.get(urr)
    htmll = driver.page_source
    soupp=BeautifulSoup(htmll,'html.parser')
    date=soupp.find("time",{"class":"fw-bold"}).get_text()
    strin=date.split("-")
    return strin[0]
#------------------------------------
def baslik(urr):
    driver.get(urr)
    htmll = driver.page_source
    soupp=BeautifulSoup(htmll,'html.parser')
    title= soupp.find("h1").get_text()
    return title
#------------------------------------
def icerik(urr):
    driver.get(urr)
    htmll = driver.page_source
    soupp=BeautifulSoup(htmll,'html.parser')
    content=' '
    iceri=soupp.find("div",{'class':'article-text container-padding'}).find_all('p')
    for u in iceri:
        content+=u.get_text()
    return content
#-----------------------------------------------------------------------------------------------------------------------
A=[]
driver.get(url)
html=driver.page_source
soup = BeautifulSoup(html,'html.parser')
list2 = soup.find_all("div", {"class": "col-lg-6"})
g=0
for i in list2:
    for link in i.find_all('a'):
        my_link = link.get('href')
        base = 'https://www.milligazete.com.tr'
        urra='{}{}'.format(base, my_link)
        try:
            k=kategori(urra)
            t=tarih(urra)
            b=baslik(urra)
            i=icerik(urra)
            l = {"Kategori":k,"Tarih":t,"Başlik":b,"İçerik":i,"Link":urra}
            g+=1
            A.append(l)
            print(g)
        except:
            pass
with open("veriler","a",encoding='utf-8') as h:
    for i in A:
        h.write(str(i)+",\n")
        print(i)