import tkinter
import xlrd
import pyperclip

销售表= xlrd.open_workbook(filename = "崂山销售登记新表.xls")
sheet1 = 销售表.sheet_by_index(0)
def 获得列序号(表名,查找字段名):
    列序号 = None
    for i in range(表名.ncols):
        if (表名.cell_value(0,i) == 查找字段名):
            列序号 = i
            break
    return 列序号
名称 = sheet1.col_values(获得列序号(sheet1,"企业名称"),1)
税号 = sheet1.col_values(获得列序号(sheet1,"税号"),1)
地址 = sheet1.col_values(获得列序号(sheet1,"注册地址、注册电话"),1)
电话 = sheet1.col_values(获得列序号(sheet1,"联系电话"),1)
银行 = sheet1.col_values(获得列序号(sheet1,"银行账号"),1)
lis1 = [名称[-1],税号[-1],地址[-1]+电话[-1],银行[-1]]
def 提取方法():
	text1.delete(1.0,tkinter.END)
	text1.insert(tkinter.INSERT,名称[-1])
	text2.delete(1.0,tkinter.END)
	text2.insert(tkinter.INSERT,税号[-1])
	text3.delete(1.0,tkinter.END)
	text3.insert(tkinter.INSERT,地址[-1]+电话[-1])
	text4.delete(1.0,tkinter.END)
	text4.insert(tkinter.INSERT,银行[-1])

def 复制(n):
	pyperclip.copy(lis1[n])



win = tkinter.Tk()
win.title("嘉怡")
win.geometry('+500+300')
win.resizable(0, 0)  #固定
win.wm_attributes('-topmost',1)  #置顶
提取 = tkinter.Button(win,width = 70,height=2,text = "世界上最沙雕的人才点这个键",command = 提取方法)
提取.grid(row=0, column=0,columnspan = 2)
text1 = tkinter.Text(win,width=50,height=3)
text1.grid(row=1, column=0)
button1 = tkinter.Button(win,width = 20,height=2,text = "点击复制",command = lambda:pyperclip.copy(lis1[0]))
button1.grid(row=1, column=1)
text2 = tkinter.Text(win,width=50,height=3)
text2.grid(row=2, column=0)
button2 = tkinter.Button(win,width = 20,height=2,text = "点击复制",command = lambda:pyperclip.copy(lis1[1]))
button2.grid(row=2, column=1)
text3 = tkinter.Text(win,width=50,height=3)
text3.grid(row=3, column=0)
button3 = tkinter.Button(win,width = 20,height=2,text = "点击复制",command = lambda:pyperclip.copy(lis1[2]))
button3.grid(row=3, column=1)
text4 = tkinter.Text(win,width=50,height=3)
text4.grid(row=4, column=0)
button4 = tkinter.Button(win,width = 20,height=2,text = "点击复制",command = lambda:pyperclip.copy(lis1[3]))
button4.grid(row=4, column=1)

win.mainloop()

