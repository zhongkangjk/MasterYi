import requests
ip = "221.0.128.42"

try:
    kv = {'ip':ip}
    kv1 = {'user-agent': 'Mozillia/5.0'}
    r = requests.get("http://www.ip138.com/ips138.asp",params = kv,headers = kv1)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("爬取失败")
