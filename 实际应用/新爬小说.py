import requests
from bs4 import BeautifulSoup

url = "https://www.biqiuge8.com/book/24276/15316323.html"
while True:
	try:
	    kv = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER'}
	    r = requests.get(url,headers = kv)
	    r.raise_for_status()
	    r.encoding = r.apparent_encoding
	    html = r.text
	except:
	    print("当时就没打开这页"+url)
	soup = BeautifulSoup(html,"html.parser")
	title = soup.select('.content > h1:nth-child(1)')[0].text
	title1 = "\r\n\r\n\r\n\r\n\r\n    "+title+"\r\n\r\n\r\n\r\n    "
	text = soup.select('#content')[0].text.split("https")[0]
	text = '\r\n\r\n    '.join(text.split())
	with open("元尊.txt",'a',encoding = 'utf-8') as f:
	    f.write(title1)
	    f.write(text)
	print(title+"下载完成")
	href = soup.select('.page_chapter > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)')[0]['href']
	url = 'https://www.biqiuge8.com' + href
	if href == '/book/24276/':
	    print("下载完成")
	    break
