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


