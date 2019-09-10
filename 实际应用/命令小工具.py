import readline
readline.parse_and_bind("control-v: paste")
import os
import time
password = input("请输入暗号")
n = 3
while password != "刘硕是沙雕":
    print("暗号错误，杀头！再给你",n,"次机会")
    password = input('''继续输入
(小提示：刘硕是什么?,打5个字)
''')
    while n > 1:
        n -= 1
        break
    else:
        time.sleep(3)
        exit()
else:
    print("""
暗号正确
请输入需要的功能：
1.屏幕键盘           10.启动QQ
2.控制面板
3.打开字体文件夹
4.打印机
5.区域和语言选项
6.防火墙设置
7.结束kp进程
8.结束newskkp进程
9.打开服务
    """)
    while 2:
        command = input()
        if command == "1":
            os.system("osk")
        elif command == "2":
            os.system("control")
        elif command == "3":
            os.system("control fonts")
        elif command == '4':
            os.system("control printers")
        elif command == '5':
            os.system("intl.cpl")
        elif command == '6':
            os.system("firewall.cpl")
        elif command == '7':
            os.system("taskkill /F /im kp.exe")
        elif command == '8':
            os.system("taskkill /F /im newskkp.exe")
        elif command == '9':
            os.system("services.msc")
        elif command == '10':
            os.system("\"C:\Program Files (x86)\Tencent\QQ\Bin\QQScLauncher.exe\"")
        elif command == '11':
            os.system("\"G:\ShadowsocksR-win-4.8.1\ShadowsocksR-dotnet4.0.exe\"")
        elif command == "cmd":
            print("本程序可以直接执行CMD无需启动")
        else:
            os.system(command)



