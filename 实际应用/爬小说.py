#coding=utf-8
import urllib.request
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER'}
def paxiaoshuo(next,url,name,a):
    a = int(a)
    while True:
        req = urllib.request.Request(url =url +next,headers =headers)
        html = urllib.request.urlopen(req).read()
        soap = BeautifulSoup(html,'html5lib')
        title = soap.title.string[0:a]
        print(title)
        title = "\r\n    "+title+'\r\n    '
        for s in soap.find_all('div', attrs={'class':'link xb'}):
            for i in s.find_all('a', attrs={'id':'book-next'}):
                next = i.get('href')
        for s in soap.find_all('div',attrs = {'id':'BookText'}):
            text = s.text
        text = '\r\n    '.join(text.split())
        with open (name,'a',encoding = 'utf8') as f:
            f.write(title)
            f.write(text)
        if next == 'index.html':
            break
paxiaoshuo('11969051.html',u'http://www.uuxs.la/book/38/38142/','龙符','-8')




'''
next = '2455874.html'
url = u'http://www.uuxs.la/book/6/6008/'
name = '天域苍穹'
a = -10
'''
