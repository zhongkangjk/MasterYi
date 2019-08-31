import requests
keyword = "python"
try:
    kv = {'wd':keyword}
    r = requests.get("http://www.baidu.com/s",params = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    #print(len(r.text))
    print(r.headers)
except:
    print("爬取失败")