import xlrd,sys,os,tkinter,win32gui,win32con,win32api,time
from tkinter import ttk


#资料引入
def resource_path(relative_path):
    '''返回资源绝对路径。'''
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller会创建临时文件夹temp
        # 并把路径存储在_MEIPASS中
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)
logo = resource_path('2.ico')
时间表路径 = resource_path('工作簿1.xlsx')
不可收路径 = resource_path('不可收.txt')
一般路径 = resource_path('可收取一般纳税人.txt')
小规模路径 = resource_path('可收取小规模.txt')
#销售表路径 = resource_path('工作簿1.xlsx')
def 找出销售表():
    namelist = os.listdir(os.getcwd())
    for x in namelist:
        if "崂山销售登记新表" in x:
            销售表路径 = x
            return 销售表路径
            break
def 找出桌面的CRM():
    namelist = os.listdir(os.path.join(os.path.expanduser('~'),"Desktop"))
    for x in namelist:
        if "GXCRM" in x:
            CRM路径 = x
            return resource_path(os.path.join(os.path.join(os.path.expanduser('~'),"Desktop"),CRM路径))
            break   


#查询程序
整行 = []
dk = xlrd.open_workbook(filename = 时间表路径)
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
    with open (不可收路径) as f:
        for line in f.readlines():
            if mingcheng in line:
                rs = line.rstrip('\n')
                return rs+"不可收"
def keshouxiaoguimo(mingcheng):
    with open (小规模路径) as f:
        for line in f.readlines():
            if mingcheng in line:
                rs = line.rstrip('\n')
                return rs+"可收取小规模"
def keshouyiban(mingcheng):
    with open (一般路径) as f:
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
        res = chazhao(entry1.get().strip())
        if "不可收" in res:
        	text1.insert(tkinter.INSERT,res,"r")
        elif "可收取" in res:
        	text1.insert(tkinter.INSERT,res,"g")
        else :
        	text1.insert(tkinter.INSERT,res)
    else :
        text1.delete(1.0,tkinter.END)
        text1.insert(tkinter.INSERT,"别闹,打了字再点")
def go2():
    entry1.delete(0,tkinter.END)
def go3(event):
    entry1.delete(0,tkinter.END)
    text1.delete(1.0,tkinter.END)







#右键模块
def cut(editor, event=None):
    editor.event_generate("<<Cut>>")
def copy(editor, event=None):
    editor.event_generate("<<Copy>>")
def paste(editor, event=None):
    editor.event_generate('<<Paste>>')
def rightKey(event, editor):
    menubar.delete(0,tkinter.END)
    menubar.add_command(label='剪切',command=lambda:cut(editor))
    menubar.add_command(label='复制',command=lambda:copy(editor))
    menubar.add_command(label='粘贴',command=lambda:paste(editor))
    menubar.post(event.x_root,event.y_root)



#基础信息填写
def 点击(id):
    win32gui.SendMessage(id,win32con.WM_LBUTTONDOWN, 0,0)
    win32gui.PostMessage(id,win32con.WM_LBUTTONUP, 0,0)
def 填信息(id,text):
    win32gui.SendMessage(id,win32con.WM_SETTEXT, 0,text)
def 发送回车(id):
    win32gui.SendMessage(id,win32con.WM_KEYDOWN, win32con.VK_RETURN,0)
    win32gui.PostMessage(id,win32con.WM_KEYUP, win32con.VK_RETURN,0)
def 列出子窗口句柄(id):
    hwndChildList = []
    win32gui.EnumChildWindows(id, lambda hwnd,param: param.append(hwnd),hwndChildList)
    #for i in hwndChildList:
        #print(i ,"{:#016X}".format(i),win32gui.GetWindowText(i))
    return hwndChildList
def 获得窗口标题的句柄(name):
    hwndChildList = []
    win32gui.EnumChildWindows(None, lambda hwnd,param: param.append(hwnd),hwndChildList)
    for i in hwndChildList:
        if name in win32gui.GetWindowText(i):
            return i
def 提取句柄文本(句柄):
    # 获取识别结果中输入框文本
    length = win32gui.SendMessage(句柄, win32con.WM_GETTEXTLENGTH)+1
    buf = win32gui.PyMakeBuffer(length)
    #发送获取文本请求
    win32api.SendMessage(句柄, win32con.WM_GETTEXT, length, buf)
    #下面应该是将内存读取文本
    address, length = win32gui.PyGetBufferAddressAndLen(buf[:-1])
    text = win32gui.PyGetString(address, length)
    return text

def 登陆():
    win32api.ShellExecute(1,'open',找出桌面的CRM(),'','',1)
    time.sleep(1)

    用户名 = 列出子窗口句柄(获得标题对应句柄('登陆 Ver2.0.0.432'))[5]
    密码 = 列出子窗口句柄(获得标题对应句柄('登陆 Ver2.0.0.432'))[4]
    确定 = 列出子窗口句柄(获得标题对应句柄('登陆 Ver2.0.0.432'))[3]
    win32gui.SendMessage(用户名,win32con.WM_SETTEXT, 0,'zhangqiang')
    win32gui.SendMessage(密码,win32con.WM_SETTEXT,0 ,'12345678')
    win32gui.SendMessage(确定,win32con.WM_LBUTTONDOWN, 0,0)
    win32gui.PostMessage(确定,win32con.WM_LBUTTONUP, 0,0)
    hwndChildList = []
    #
    time.sleep(2)
    当日提示 = win32gui.FindWindow(None, "当日提示")
    print(当日提示)

    if 当日提示:
        print("找到句柄了")
        win32gui.EnumChildWindows(当日提示, lambda hwnd,param: param.append(hwnd),hwndChildList)
        关闭 = hwndChildList[-1]
        time.sleep(1)
        win32gui.SendMessage(关闭,win32con.WM_LBUTTONDOWN, 0,0)
        win32gui.SendMessage(关闭,win32con.WM_LBUTTONUP, 0,0)
    else:
        print("not found")


def 基础资料判断():

    for i in 基础资料:
        if i[1] == 下拉菜单.get():
            判断税号 = i[2]
            hwndChildList = []
            win32gui.EnumChildWindows(None, lambda hwnd,param: param.append(hwnd),hwndChildList)
            for i in hwndChildList:
                if '基础资料修改' in win32gui.GetWindowText(i):
                    CRM = i
            hwndChildList = []
            win32gui.EnumChildWindows(CRM, lambda hwnd,param: param.append(hwnd),hwndChildList)
            需判断的识别号 = hwndChildList[58]
            进行判断 = hwndChildList[54]
            填信息(需判断的识别号,判断税号)
            点击(进行判断)
            #print(win32gui.GetWindowText(hwndChildList[14]))

基础资料 = []
基础资料名称 = []
基础资料全部 = []
def 获取基础资料():
    win.wm_attributes('-topmost',1)  #置顶
    销售表文件 = xlrd.open_workbook(filename = 找出销售表())
    销售表1 = 销售表文件.sheet_by_index(0)
    for i in range(销售表1.nrows-20,销售表1.nrows):
        基础资料名称.append(销售表1.row_values(i)[1])
        基础资料.append(销售表1.row_values(i))
    for j in range(0,销售表1.nrows):
        基础资料全部.append(销售表1.row_values(j))
    下拉菜单['value'] = 基础资料名称[::-1]





续费资料 = []
续费资料名称 = []
def 获取续费资料():
    获取基础资料()
    win.wm_attributes('-topmost',1)  #置顶
    销售表文件 = xlrd.open_workbook(filename = 找出销售表())
    续费表 = 销售表文件.sheet_by_index(1)
    for i in range(续费表.nrows-20,续费表.nrows):
        续费资料名称.append(续费表.row_values(i)[2])
        续费资料.append(续费表.row_values(i))
    续费下拉菜单['value'] = 续费资料名称[::-1]


def 开始填写基础资料():
    for i in 基础资料:
        if i[1] == 下拉菜单.get():
            客户名称 = i[1]
            经营地址 = i[5]
            办税人员 = i[3]
            办公地区域 = '370212 崂山'
            所属区域 = '370212崂山'
            电话 = i[4]
            纳税人类别 = i[14] + '纳税人'
            hwndChildList = []
            win32gui.EnumChildWindows(None, lambda hwnd,param: param.append(hwnd),hwndChildList)
            for i in hwndChildList:
                if '基础资料修改' in win32gui.GetWindowText(i):
                    CRM = i
            hwndChildList = []
            win32gui.EnumChildWindows(CRM, lambda hwnd,param: param.append(hwnd),hwndChildList)
            客户名称位置 = hwndChildList[14]
            经营地址位置 = hwndChildList[13]
            办税人员位置 = hwndChildList[10]
            办公地区域位置 = hwndChildList[8]
            电话位置 = hwndChildList[44]
            纳税人类别位置 = hwndChildList[6]
            所属区域位置 = hwndChildList[50]
            填信息(客户名称位置,客户名称)
            填信息(经营地址位置,经营地址)
            填信息(办税人员位置,办税人员)
            填信息(办公地区域位置,办公地区域)
            填信息(电话位置,电话)
            填信息(纳税人类别位置,纳税人类别)
            填信息(所属区域位置,所属区域)
            点击(hwndChildList[51])
def 点击新增():
    hwndChildList = []
    win32gui.EnumChildWindows(None, lambda hwnd,param: param.append(hwnd),hwndChildList)
    for i in hwndChildList:
        if '基础资料修改' in win32gui.GetWindowText(i):
            CRM = i
    hwndChildList = []
    win32gui.EnumChildWindows(CRM, lambda hwnd,param: param.append(hwnd),hwndChildList)
    新增 = hwndChildList[15]
    点击(新增)

#产品销售

def 获得产品销售总窗口句柄():
    hwndChildList = []
    win32gui.EnumChildWindows(None, lambda hwnd,param: param.append(hwnd),hwndChildList)
    for i in hwndChildList:
        if '产品销售' in win32gui.GetWindowText(i):
            return i
def 获得标题对应句柄(name):
    hwndChildList = []
    win32gui.EnumChildWindows(获得产品销售总窗口句柄(), lambda hwnd,param: param.append(hwnd),hwndChildList)
    for i in hwndChildList:
        if name == win32gui.GetWindowText(i):
            return i
def 点新开户():
    点击(获得标题对应句柄('新开户'))
def 产品销售查询():
    for i in 基础资料:
        if i[1] == 下拉菜单.get():
            客户名称 = i[1]
            填信息(列出子窗口句柄(获得标题对应句柄('产品销售'))[-2],客户名称)
            发送回车(列出子窗口句柄(获得标题对应句柄('产品销售'))[-2])
def 产品销售填写():
    #选择业务员
    win32api.SendMessage(列出子窗口句柄(获得标题对应句柄('新开户销售'))[19], win32con.CB_SETCURSEL,76,  0)
    win32api.SendMessage(获得标题对应句柄('新开户销售'), win32con.WM_COMMAND, 0x90000, 列出子窗口句柄(获得标题对应句柄('新开户销售'))[19])
    win32api.SendMessage(获得标题对应句柄('新开户销售'), win32con.WM_COMMAND, 0x10000, 列出子窗口句柄(获得标题对应句柄('新开户销售'))[19])
    #
    纳税人类别字典 = {'一般':0,'小规模':1}
    for i in 基础资料:
        if i[1] == 下拉菜单.get():
            #纳税人类别
            纳税人类别 = i[14]
            win32api.SendMessage(列出子窗口句柄(获得标题对应句柄('销售回款'))[37], win32con.CB_SETCURSEL,纳税人类别字典[纳税人类别],  0)
            win32api.SendMessage(列出子窗口句柄(获得标题对应句柄('销售回款'))[35], win32con.WM_COMMAND, 0x90000, 列出子窗口句柄(获得标题对应句柄('销售回款'))[37])
            win32api.SendMessage(列出子窗口句柄(获得标题对应句柄('销售回款'))[35], win32con.WM_COMMAND, 0x10000, 列出子窗口句柄(获得标题对应句柄('销售回款'))[37])
            经办人 = i[3]
            经办人位置 = 列出子窗口句柄(获得标题对应句柄('个人会员信息'))[0]
            填信息(经办人位置,经办人)
            经办人电话 = i[4]
            经办人电话位置 = 列出子窗口句柄(获得标题对应句柄('个人会员信息'))[1]
            填信息(经办人电话位置,经办人电话)
            税控盘编号 = i[7]
            税控盘编号位置 = 列出子窗口句柄(获得标题对应句柄('百旺信息'))[3]
            填信息(税控盘编号位置,税控盘编号)
            报税盘编号 = '00000000000'
            报税盘编号位置 = 列出子窗口句柄(获得标题对应句柄('百旺信息'))[1]
            填信息(报税盘编号位置,报税盘编号)
            空 = ''
            空位置 = 列出子窗口句柄(获得标题对应句柄('新开户销售'))[13]
            填信息(空位置,空)
            税控盘发票 = i[9]
            税控盘发票位置 = 列出子窗口句柄(获得标题对应句柄('新开户销售'))[9]
            填信息(税控盘发票位置,税控盘发票)
            服务费发票 = i[10]
            服务费发票位置 = 列出子窗口句柄(获得标题对应句柄('新开户销售'))[3]
            填信息(服务费发票位置,服务费发票)
def 续费查询():
    for i in 续费资料:
        if i[2] == 续费下拉菜单.get():
            客户名称 = i[2]
            填信息(列出子窗口句柄(获得标题对应句柄('产品销售'))[-2],客户名称)
            发送回车(列出子窗口句柄(获得标题对应句柄('产品销售'))[-2])
def 续费填写():
    #选择销售类别
    win32api.SendMessage(列出子窗口句柄(获得标题对应句柄('销售信息'))[-2], win32con.CB_SETCURSEL,13,  0)
    win32api.SendMessage(获得标题对应句柄('销售信息'), win32con.WM_COMMAND, 0x90000, 列出子窗口句柄(获得标题对应句柄('销售信息'))[-2])
    win32api.SendMessage(获得标题对应句柄('销售信息'), win32con.WM_COMMAND, 0x10000, 列出子窗口句柄(获得标题对应句柄('销售信息'))[-2])
    for i in 续费资料:
        if i[2] == 续费下拉菜单.get():
            续费发票号码 = i[8]
            续费发票号码位置 = 列出子窗口句柄(获得标题对应句柄('销售信息'))[-3]
            填信息(续费发票号码位置,续费发票号码)
            续费报税盘编号 = '00000000000'
            续费报税盘编号位置 = 列出子窗口句柄(获得标题对应句柄('百旺信息'))[-3]
            填信息(续费报税盘编号位置,续费报税盘编号)
            for x in 基础资料全部:
                if i[2] == x[1]:
                    续费税控盘编号 = x[7]
                    print(续费税控盘编号)
                    续费税控盘编号位置 = 列出子窗口句柄(获得标题对应句柄('百旺信息'))[-1]
                    填信息(续费税控盘编号位置,续费税控盘编号)

def 新增新开户记录():
    点击(获得标题对应句柄('增加销售记录'))
def 新增续费记录():
    点击(获得标题对应句柄('增加销售记录'))
    #text2.delete(1.0,tkinter.END)
    text2.insert(1.0,续费下拉菜单.get() + '续费已点击增加' +'\r\n')





#窗口显示
win = tkinter.Tk()
win.iconbitmap(logo)
win.title("查询企业V191121")
win.geometry('450x150+600+300')
#win.resizable(0, 0)  #固定位置
menubar = tkinter.Menu(win,tearoff=False)#创建一个菜单

tabControl = ttk.Notebook(win)


#tab1
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='查询是否可收')

frame1 = tkinter.Frame(tab1)
frame2 = tkinter.Frame(tab1)
frame1.pack()
frame2.pack()

label = tkinter.Label(frame1,text = '请在此输入企业名称：')
label.pack(side='left')

entry1 = tkinter.Entry(frame1,width = 35)
entry1.pack(side='left')
entry1.focus()
entry1.bind('<Return>',go)
entry1.bind('<Delete>',go3)
entry1.bind("<Button-3>", lambda x: rightKey(x, entry1))#绑定右键鼠标事件

tkinter.Button(frame1,text = "查询", command = go).pack(side='left')
tkinter.Button(frame1,text = "清除", command = go2).pack()

text1 = tkinter.Text(frame2,height=10)
text1.tag_config('r', foreground='red')
text1.tag_config('g', foreground='green')
text1.bind("<Button-3>", lambda x: rightKey(x, text1))#绑定右键鼠标事件
text1.pack()


#tab2


tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='CRM填写')

frame3 = tkinter.Frame(tab2)
frame4 = tkinter.Frame(tab2)
frame5 = tkinter.Frame(tab2)
frame6 = tkinter.Frame(tab2)
frame7 = tkinter.Frame(tab2)
frame8 = tkinter.Frame(tab2)
frame6.pack()
frame3.pack()
frame7.pack()
frame4.pack()
frame8.pack()
frame5.pack()


tkinter.Label(frame6,text = '基础资料模块').pack()

#基础资料模块


tkinter.Button(frame3,text = "刷新资料", command = 获取基础资料).pack(side = 'left')
下拉菜单 = ttk.Combobox(frame3)
下拉菜单.pack(side = 'left')
下拉菜单['value'] = ['请选择公司名称']
下拉菜单.current(0)
tkinter.Button(frame3,text = "肉眼判断是否存在", command = 基础资料判断).pack(side = 'left')
tkinter.Button(frame3,text = "开始填写",command = 开始填写基础资料).pack(side = 'left')
tkinter.Button(frame3,text = "点击新增",command = 点击新增).pack(side = 'left')

tkinter.Label(frame7,text = '产品销售模块',justify = "left").pack()
#产品销售模块

tkinter.Button(frame4,text = "产品销售查询", command = 产品销售查询,width=15).pack(side = 'left')
tkinter.Button(frame4,text = "新开户", command = 点新开户,width=10).pack(side = 'left')
tkinter.Button(frame4,text = "填写", command = 产品销售填写,width=14).pack(side = 'left')
tkinter.Button(frame4,text = "新增销售记录", command = 新增新开户记录,width=40).pack(expand = 'yes',fill = 'both')



#





#tab3
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='续费模块')
frame5 = tkinter.Frame(tab3)
frame8 = tkinter.Frame(tab3)
frame5.pack()
frame8.pack()


#续费模块
tkinter.Button(frame5,text = "刷新资料", command = 获取续费资料 ).pack(side = 'left')
续费下拉菜单 = ttk.Combobox(frame5)
续费下拉菜单.pack(side = 'left')
续费下拉菜单['value'] = ['请选择公司名称']
续费下拉菜单.current(0)
tkinter.Button(frame5,text = "续费查询", command = 续费查询 ).pack(side = 'left')
tkinter.Button(frame5,text = "续费填写", command = 续费填写 ).pack(side = 'left')
tkinter.Button(frame5,text = "新增续费记录", command = 新增续费记录,width=20 ).pack(side = 'left')

text2 = tkinter.Text(frame8,height=6)
text2.bind("<Button-3>", lambda x: rightKey(x, text2))#绑定右键鼠标事件
text2.pack()


def 搞电话():
    file = open("短信.txt", 'a')
    企业名称列表 = []
    with open("企业名称.txt", encoding='utf8') as f:
        for line in f.readlines():
            企业名称列表.append(line.rstrip('\n'))
    for i in 企业名称列表:
        填信息(列出子窗口句柄(获得窗口标题的句柄('客户回访'))[75], i)
        发送回车(列出子窗口句柄(获得窗口标题的句柄('客户回访'))[75])
        电话 = 提取句柄文本(列出子窗口句柄(获得窗口标题的句柄('客户回访'))[128])
        if 电话:
            file.write(i + 电话 + '\n')
        else:
            file.write(i + '没有电话' + '\n')
        time.sleep(1)
    file.close()

tab4 = ttk.Frame(tabControl)
tabControl.add(tab4,text = '临时')
tkinter.Button(tab4,text = "临时按钮", command = 搞电话 ).pack(side = 'left')


#tab10
tab10 = ttk.Frame(tabControl) 
tabControl.add(tab10, text='更新日志')
tkinter.Label(tab10, text='''
----20191121----
增加了日志记录，但是只记录是否点击，到底录没录上不知道 
----20191120----
增加了CRM模块
----20191118----
增加了产品销售
----20191106----
增加了基础资料填写
----20191106----
打包了数据
----20191030----
忽略名称前后空格

'''
).pack()


tabControl.pack()
win.mainloop()



