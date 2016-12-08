from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random


# html=urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsobj=BeautifulSoup(html,"lxml")
# for link in bsobj.find_all("a"):
#     if "href" in link.attrs:
#         print(link.attrs["href"])

# for link in bsobj.find("div",{"id":"bodyContent"}).find_all("a",href=re.compile("^(/wiki/)((?!:).)*$")):
#     if "href" in link.attrs:
#         print(link.attrs["href"])

# random.seed(datetime.datetime.now())
# def getlinks(articleUrl):
#     html=urlopen("http://en.wikipedia.org"+articleUrl)
#     bsobj=BeautifulSoup(html,"lxml")
#     return bsobj.find("div",{"id":"bodyContent"}).find_all("a",href=re.compile("^(/wiki/)((?!:).)*$"))
#
# links=getlinks("/wiki/Kevin_Bacon")
#
# while len(links)>0:
#     newArticle=links[random.randint(0,len(links)-1)].attrs["href"]
#     print(newArticle)
#     links=getlinks(newArticle)

pages =set()
i = 0
def getlinks(pageUrl):
    print(str(len(pages)))
    global pages
    url="http://en.wikipedia.org"+pageUrl
    html=urlopen(url)
    print("页面"+url+"\n")
    bsobj=BeautifulSoup(html,"lxml")
    # try:
    #     print(bsobj.h1.get_text())
    #     #print(bsobj.find(id="mw-content-text").find_all("p")[0])
    #     #print(bsobj.find(id="ca-edit").find("span").attrs["href"])
    # except AttributeError:
    #     print("页面缺少一些属性，不用担心！")
    allurl=bsobj.find_all("a",href=re.compile("^(/wiki/)"))
    print("连接总数："+str(len(allurl)))
    for link in allurl:
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                #新页面
                newPage=link.attrs["href"]
                #i=i+1
                #print("页数："+str(i)+"\n")
                print("-----------------"+url+newPage)
                pages.add(newPage)
                getlinks(newPage)


getlinks("")
