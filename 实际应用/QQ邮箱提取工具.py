import tkinter
import re
QQstr = '''
this is QQ 
'''
baklist = None

def go():
    mylist = re.findall("[1-9]\\d{5,10}",text.get("0.0","end"))
    global baklist
    baklist = []
    for qq in mylist:
        qq += "@qq.com"
        list.insert(tkinter.END,qq)
        baklist.append(qq)
    pass
def save():
    file = open(r"C:\Users\Administrator\Desktop\项目2\1.txt","wb")
    if baklist != None:
        for QQ in baklist:
            file.write((QQ + "\r\n").encode("utf-8"))
    file.close()
win = tkinter.Tk()
button = tkinter.Button(win,text = "提取",command = go)
button.pack()
button2 = tkinter.Button(win,text = "保存",command = save)
button2.pack()
text = tkinter.Text(win)
text.insert(tkinter.END,QQstr)
text.pack()
list = tkinter.Listbox(win)
list.pack()
win.mainloop()
