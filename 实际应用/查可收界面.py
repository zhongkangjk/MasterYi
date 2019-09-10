import tkinter

from tkinter import ttk
import xlrd
dk = xlrd.open_workbook(filename = "工作簿1.xlsx")
sheet1 = dk.sheet_by_index(0)
def 获得列序号(表名,查找字段名):
    列序号 = None
    for i in range(表名.ncols):
        if (表名.cell_value(0,i) == 查找字段名):
            列序号 = i
            break
    return 列序号
名称列 = sheet1.col_values(获得列序号(sheet1,"名称"),2)
服务期限 = sheet1.col_values(获得列序号(sheet1,"服务期限"),2)
整行 = []
for x in range(0,len(名称列)):
    整行.append(名称列[x]+服务期限[x])

def chashijian(mingcheng):
    result = []
    for dange in 整行:
        if mingcheng in dange:
            result.append(dange)
    if result != []:
        return result[0]+"到期\n"
    else:
        result.append("今年到期表没有\n")
        return result[0]
def bukeshou(mingcheng):
    with open ("不可收.txt") as f:
        for line in f.readlines():
            if mingcheng in line:
                rs = line.rstrip('\n')
                return rs+"不可收"
def keshouxiaoguimo(mingcheng):
    with open ("可收取小规模.txt") as f:
        for line in f.readlines():
            if mingcheng in line:
                rs = line.rstrip('\n')
                return rs+"可收取小规模"
def keshouyiban(mingcheng):
    with open ("可收取一般纳税人.txt") as f:
        for line in f.readlines():
            if mingcheng in line:
                rs = line.rstrip('\n')
                return rs+"可收取一般纳税人"
def chazhao(mingcheng):
    if bukeshou(mingcheng) == None:
        if keshouxiaoguimo(mingcheng) == None:
            if keshouyiban(mingcheng) == None:
                return chashijian(mingcheng)+"是否可收三个表里都没有"
            else:
                return chashijian(mingcheng)+keshouyiban(mingcheng)
        else:
            return chashijian(mingcheng)+keshouxiaoguimo(mingcheng)
    else:
        return chashijian(mingcheng)+bukeshou(mingcheng)
def go(event):
    if entry1.get() != "":
        text1.delete(1.0,tkinter.END)
        text1.insert(tkinter.INSERT,chazhao(entry1.get()))
    else :
        text1.delete(1.0,tkinter.END)
        text1.insert(tkinter.INSERT,"别闹,打了字再点")
def go1():
    if entry1.get() != "":
        text1.delete(1.0,tkinter.END)
        text1.insert(tkinter.INSERT,chazhao(entry1.get()))
    else :
        text1.delete(1.0,tkinter.END)
        text1.insert(tkinter.INSERT,"别闹,打了字再点")
def go2():
    entry1.delete(0,tkinter.END)
def go3(event):
    entry1.delete(0,tkinter.END)
    text1.delete(1.0,tkinter.END)
win = tkinter.Tk()
win.title("宇宙超级无敌小程序帅比专用V190829")
win.geometry('450x126+600+300')
tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)


tab1.pack()
tabControl.add(tab1, text='查询是否可收')

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='待开发')
tabControl.pack()

frame1 = tkinter.Frame(tab1)
frame2 = tkinter.Frame(tab1)

frame1.pack()
frame2.pack()
win.resizable(0, 0)
label = tkinter.Label(frame1,text = '请在此输入企业名称：')
label.pack(side='left')
entry1 = tkinter.Entry(frame1,width = 35)
entry1.pack(side='left')
entry1.focus()
entry1.bind('<Return>',go)
entry1.bind('<Delete>',go3)
tkinter.Button(frame1,text = "查询", command = go1).pack(side='left')
tkinter.Button(frame1,text = "清除", command = go2).pack()

text1 = tkinter.Text(frame2,height=5)
text1.pack()
win.mainloop()
