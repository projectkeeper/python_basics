import requests

from bs4 import BeautifulSoup

#Webページを取得して解析する
url= "https://www.ymori.com/books/python2nen/test1.html"

html = requests.get(url)

soup = BeautifulSoup(html.content, "html.parser")

#HTML全体を表示する
#print(soup)

#print(soup.find("title"))
#print(soup.find("head"))
print(soup.find("body"))

#print(soup.find("title").text)
#print(soup.find("head").text)
print(soup.find("body").text)

