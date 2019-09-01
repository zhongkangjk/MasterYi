import requests
from bs4 import BeautifulSoup
#https://www.biqiuge.com/book/4772/2940354.html    没解决  解决了是pycharm显示不全
url = "https://www.nbiquge.com/0_127/45735.html"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER'}
try:
    r = requests.get(url,headers = headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
except:
    print("爬取失败")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")

print(soup)
