from bs4 import BeautifulSoup
import requests

url = "https://www.nbiquge.com/0_127/45735.html"
r = requests.get(url)
r.encoding = r.apparent_encoding
html = r.text
soup = BeautifulSoup(html,"html.parser")#lxml html5lib
print(soup)
#soup.a
#soup.a.string
#soup.a.attrs