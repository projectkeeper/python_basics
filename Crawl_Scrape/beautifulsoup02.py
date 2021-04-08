import requests

from bs4 import BeautifulSoup

#Webページを取得して解析する
url= "https://www.ymori.com/books/python2nen/test2.html"

html = requests.get(url)

soup = BeautifulSoup(html.content, "html.parser")

#filename="dw_beautifulsoup02.txt"

#with open(filename,mode="w") as f:
#f.write(soup.text)

for ele in soup.find_all("li"):
    print(ele.text)
#print(ele.text)
#HTML全体を表示する
#print(soup)

#print(soup.find("title"))
#print(soup.find("head"))
#print(soup.find("body"))

#print(soup.find("title").text)
#print(soup.find("head").text)
#print(soup.find("body").text)
