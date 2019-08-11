import requests
import os
url = "https://img.speedo.com.cn/resources/images/201907/landingpage-interesting/pc/banner-1.jpg"
root = "D://pics//"
path = root +url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,"wb") as f:
            f.write(r.content)
        print("文件保存成功")
    else:
        print("文件已存在")
except:
    print('爬取失败')