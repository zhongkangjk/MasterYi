import pymysql


try:
    db = pymysql.connect("127.0.0.1","root","jichidoubi666")#连接数据库
    cursor = db.cursor()#数据的游标
    #cursor.execute("SELECT VERSION()")#数据库类型
    data = cursor.fetchall()
    print(data)
    db.close()
    print("密码正确")
except:
    print("密码错误")