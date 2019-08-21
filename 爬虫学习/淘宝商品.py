import requests
import re

def getHTMLText(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER',
            "cookie":"hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; enc=sjA56zcJ9u%2F8HHfzWeGenkosE0sTJKOlrlE3PMUsXa4T4ucIGh7utUvQoTVW1UqNtT0z0zaGdAm6xBhWgTSwhQ%3D%3D; miid=202266272065909521; tracknick=zhongkangtb; _cc_=U%2BGCWk%2F7og%3D%3D; tg=0; cna=Q8BkEwdNjwACASrHh4ywLeIq; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; t=495b1ae6d656f25318235b91cf412b1a; cookie2=1e352b66734f3c1b206751d815d354ed; v=0; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; _tb_token_=e53945567abe7; mt=ci%3D-1_1; JSESSIONID=694C8BC65EFD5DCBCB5BD0FFFF0A8D54; isg=BOXl0kSA1LkPtzG_hnKhESi05qHfioaHPErXpufJqJwr_gRwr3FyhCfciCItfrFs; l=cBIvTKdVvmfdhDbzBOfZVuI81hQtoQ908sPzw4swkICP9wCH50UfWZeIGwLMCnGVK6SDR3Sq8BObB0LNuyCqJxpsw3k_J_f.."
        }
        r = requests.get(url,headers = headers,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取失败")
def parsePage(ilt,html):
    try:
        tlt = re.findall(r'"raw_title":".*?"',html)
        plt = re.findall(r'"view_price":"[\d\.]*"',html)
        #tlt = re.findall(r'\"raw_title\"\:\"[\d\.]*\"',html)
        #plt = re.findall(r'\"view_price\"\:\".*?\"',html)
        for i in range(len(tlt)):
            title = eval(tlt[i].split(":")[1])
            price = eval(plt[i].split(":")[1])
            ilt.append([title,price])
    except:
        print("获取价格或者名称失败")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","名称","价格"))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count,g[0],g[1]))
def main():
    goods = "机械键盘"
    depth = 1
    start_url = "https://s.taobao.com/search?q=" + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + "&s=" +str(44*i)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)
main()