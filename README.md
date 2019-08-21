我的笔记
====
20190810
----
requests的一个爬取网页的通用代码框架
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"
        
20190812
----
BeautifulSoup
标签树的下行遍历
.contents#将<tag>所有子节点存入列表
.children#子节点的迭代类型
.descenants#子孙节点的迭代类型
标签树的上行遍历
.parent#节点的父标签
.parents#节点先辈标签的迭代类型
标签树的平行遍历
.next_sibling#返回按照HTML文本顺序的下一个平行标签
.previous_sibling#返回按照HTML文本顺序的上一个平行标签
.next_siblings#迭代类型后续所有平行节点标签
.previous_sibling#迭代类型前续所有平行节点标签
bs4库的prettify()方法  加空格

20190821
----
正则表达式
字母和数字表示他们自身。一个正则表达式模式中的字母和数字匹配同样的字符串。
多数字母和数字前加一个反斜杠时会拥有不同的含义。
标点符号只有被转义时才匹配自身，否则它们表示特殊的含义。
反斜杠本身需要使用反斜杠转义。
由于正则表达式通常都包含反斜杠，所以你最好使用原始字符串来表示它们。模式元素(如 r'\t'，等价于 \\t )匹配相应的特殊字符。

