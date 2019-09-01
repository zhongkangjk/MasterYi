from bs4 import BeautifulSoup
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

soup=BeautifulSoup(html,"lxml") #"lxml解析方式"
soup1=BeautifulSoup(html,"html.parser") #常规网页解析，
#soup=BeautifulSoup(html,"html5lib") #HTML5解析 ,只是解析方法不一样，结果一样

print(soup.head.contents)  #contents返回一个元素下的所有子节点，列表
print(soup.body.contents)
print(soup.body.contents[1])

print(soup.head.children)  #children返回子节点
#<listiterator object at 0x7f71457f5710>
for child in soup.body.children:
    print(child)

for child in soup.descendants: #所有的孩子节点与孙子节点
    print(child)