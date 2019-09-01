import requests
from lxml import etree

url = "https://www.nbiquge.com/0_127/45735.html"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER'}
try:
    r = requests.get(url,headers = headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
except:
    print("爬取失败")
#print(r.text)

html = etree.HTML(r.text)
res = html.xpath("//h1/text()")
print(res)

'''
print html.xpath("//li/@class") #取出li的所有节点class名称
print html.xpath("//li/@text") #为空，如果包含这个属性，
print html.xpath("//li/a") #li下面5个节点，每个节点对应一个元素
print html.xpath("//li/a/@href") #取出li的所有节点 a内部href名称
print html.xpath("//li/a/@href=\"link3.html\"") #判断是有一个节点==link3.html
print html.xpath("//li//span") #取出li下面所有的span
print html.xpath("//li//span/@class") #取出li下面所有的span内部的calss
print html.xpath("//li/a//@class") #取出li的所有节点内部节点a包含的class
print html.xpath("//li") #取出所有节点
print html.xpath("//li[1]") #取出第一个
print html.xpath("//li[last()]") #取出最后一个
print html.xpath("//li[last()-1]") #取出倒数第2个
print html.xpath("//li[last()-1]/a/@href") #取出倒数第2个的a下面的href
print html.xpath("//*[@text=\"3\"]") #选着text=3的元素
print html.xpath("//*[@text=\"3\"]/@class") #选着text=3的元素
print html.xpath("//*[@class=\"nimei\"]") #选着text=3的元素
print html.xpath("//li/a/text()")#取出<>
print html.xpath("//li[3]/a/span/text()") #取出内部<>数据
'''

