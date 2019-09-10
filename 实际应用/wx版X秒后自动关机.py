import wx
import os
from subprocess import run
def guanji(canshu):
    time = path_text.GetValue()
    run("shutdown -s -t "+time,shell=True)

def quxiao(aa):
    run("shutdown -a",shell=True)

app = wx.App()
frame = wx.Frame(None,title = "自动关机",pos = (1000,200),size = (350,100))
panel = wx.Panel(frame)#面板
path_text = wx.TextCtrl(panel,size = (100,24))
open_button = wx.Button(panel,label = "启动")
open_button.Bind(wx.EVT_BUTTON,guanji)
save_button = wx.Button(panel,label = "取消")
save_button.Bind(wx.EVT_BUTTON,quxiao)
box = wx.BoxSizer()# 不带参数表示默认实例化一个水平尺寸器
box.Add(path_text,proportion = 4 ,flag = wx.EXPAND|wx.ALL,border = 3)
box.Add(open_button,proportion = 2 ,flag = wx.EXPAND|wx.ALL,border = 3)
box.Add(save_button,proportion = 2 ,flag = wx.EXPAND|wx.ALL,border = 3)
    #proportion：相对比例
    #flag：填充的样式和方向,wx.EXPAND为完整填充，wx.ALL为填充的方向
    #border：边框
box1 = wx.BoxSizer(wx.VERTICAL)#垂直尺寸器
box1.Add(box,proportion = 4 ,flag = wx.EXPAND|wx.ALL,border = 3)
panel.SetSizer(box1)

frame.Show()
app.MainLoop()
