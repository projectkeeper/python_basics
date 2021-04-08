import requests
from bs4 import BeautifulSoup
import urllib

#Webページを取得して解析する
original_url= "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(original_url)

soup = BeautifulSoup(html.content, "html.parser")

#ファイルを書き込みモードで開く
filename = "linklist.txt"

with open(filename, "w") as f:
    #すべてのaタグを検索し、リンクを絶対URLで書き出す
    for ele in soup.find_all("a"):
        print(ele.text)
        url = ele.get("href")
        url_full=urllib.parse.urljoin(original_url,url)
        print(url+"\n")
        print(url_full+"\n")
        f.write(ele.text+"\n")
        f.write(url_full+"\n")
        f.write("\n")
