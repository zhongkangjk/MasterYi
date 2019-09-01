from bs4 import BeautifulSoup
import re
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters;
and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- E
lsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie<
/a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tilli
e</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""


soup=BeautifulSoup(html,"html5lib") #HTML5解析 ,只是解析方法不一样，结果一样
print(soup.find("p"))   #查找第一个标签
print(soup.find_all("p"))#查找所有标签
print(soup.find_all("p")[2]) #查找所有标签第三个

for tag in soup.find_all(re.compile("^t")): #正则表达式提取
    print(tag.name)

print(soup.find_all(["title", "body"])) #按照列表，有一个符合条件即可
print(soup.find_all(id='link2'))  #按照id
print(soup.find_all("a",class_='link2')) #限定查找a标签的class

print(soup.find_all(text='The Dormouse\'s story'))  #精确等于
soup.find_all(text=["Tillie", "Elsie", "Lacie"]) #其中一个满足即可
# [u'Elsie', u'Lacie', u'Tillie']
soup.find_all(text=re.compile("Dormouse")) #正则表达式