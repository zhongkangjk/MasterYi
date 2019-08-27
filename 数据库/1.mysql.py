import pymysql


try:
    db = pymysql.connect("127.0.0.1","root","jichidoubi666")#连接数据库
    cursor = db.cursor()#数据的游标
    #cursor.execute("SELECT VERSION()")#数据库类型
    cursor.execute('use xiaomi')
    cursor.execute('select * from xiaomi_com where id <1000')
    data = cursor.fetchall()#查询的结果
    print(data)
    db.close()
    print("密码正确")
except:
    print("密码错误")