import requests
url = "https://www.amazon.cn/dp/B01I2JGBMQ/ref=sr_1_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&keywords=python&qid=1565515291&s=books&sr=1-1"
try:
    kv = {'user-agent': 'Mozillia/5.0'}
    r = requests.get(url,headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")


