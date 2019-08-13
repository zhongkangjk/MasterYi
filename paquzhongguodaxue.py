import requests
from bs4 import BeautifulSoup
import bs4
def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])
'''
def printUnivList(ulist,num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名","学校名称","总分"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}").format(u[0],u[1],u[2])
         #print('suc' + str(num))
'''
def printUnivList(ulist,num):#将ulist的信息打印出来
    tplt = '{0:^10}\t{1:{3}^10}\t{2:^10}'#生成一个输出模板的变量，主要增加中间的宽度设定，将学校名称的地方增加为10，
    print(tplt.format('排名','学校名称','总分',chr(12288)))#用print实现了对表头的打印,输出字符串替换成tplt,增加中文空格的变量位置
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))#将第i个学校的信息做为一个简短的变量u来代替
    #print('suc' + str(num))#num表示你希望将列表中多少个元素多少个信息打印出来



def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20) #20Univ
main()