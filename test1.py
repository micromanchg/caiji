from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# html=urlopen("http://pythonscraping.com/pages/page1.html")
# bsobj=BeautifulSoup(html.read(),'lxml')
# print(bsobj.h1)
#
# html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# bsobj=BeautifulSoup(html,"lxml")
# namelist=bsobj.find_all("span",{"class":"green"})
# namelist1=bsobj.find_all(text="the prince")
# print(len(namelist1))
# for name in namelist:
#     print(name.get_text())
#
# alltext=bsobj.find_all(id="text")
# print(len(alltext))
# for text in alltext:
#     print(text.get_text())

# html=urlopen("http://www.pythonscraping.com/pages/page3.html")
# bsobj=BeautifulSoup(html,"lxml")
# for child in bsobj.find("table",{"id":"giftlist"}):
#     print(child)

html=urlopen("http://www.pythonscraping.com/pages/page3.html")
bsobj=BeautifulSoup(html,"lxml")
images=bsobj.find_all("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image["src"])