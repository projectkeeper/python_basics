import requests
from bs4 import BeautifulSoup

#Webページを取得して解析する
url= "https://www.yahoo.co.jp/"
html = requests.get(url)

soup = BeautifulSoup(html.content, "html.parser")

news_topic = soup.find(id="tabpanelTopics1")

for ele in news_topic.find_all("a"):
    print(ele.text)
    url = ele.get("href")
    print(url+"\n")
#print(news_topic)
#print(news_topic.text)
