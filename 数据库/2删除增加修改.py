import pymysql


try:
    db = pymysql.connect("127.0.0.1","root","jichidoubi666")#连接数据库
    cursor = db.cursor()#数据的游标

    cursor.execute('use xiaomi')
    #cursor.execute("delete  from xiaomi_com where username = 'jichidoubi'")#删除
    #cursor.execute("insert into leibusi values(1,'gaozhonghua',1594159)")#增加
    cursor.execute("update  leibusi set username= 'gaoqinghua' where username = 'gaozhonghua'")#更改
    db.commit()#生效

    db.close()
    print("密码正确")
except:
    print("密码错误")