import requests
from bs4 import BeautifulSoup

#Webページを取得して解析する
url= "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(url)

soup = BeautifulSoup(html.content, "html.parser")
chap = soup.find(id="chap2")

print(chap)
print(chap.text)

for ele in chap.find_all("li"):
    print(ele)

for ele in chap.find_all("li"):
    print(ele.text)
