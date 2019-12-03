import re
i = '''
,"raw_title":"雷柏V500机械键盘青轴黑轴台式笔记本电脑吃鸡键盘电竞游戏键盘","pic_url":"//g-search1.alicdn.com/img/bao/uploaded/i4/i2/249789133/O1CN01xyd4Q32HKxlYWMpeE_!!0-item_pic.jpg","detail_url":"//detail.tmall.com/item.htm?id\u003d38405732513\u0026ad_id\u003d\u0026am_id\u003d\u0026cm_id\u003d140105335569ed55e27b\u0026pm_id\u003d\u0026abbucket\u003d15","view_price":"95.00","view_fee":"0.00"
'''
title = re.findall(r'"raw_title":".*?"',i)
price = re.findall(r'"view_price":"[\d\.]*"',i)
print(title,price)
