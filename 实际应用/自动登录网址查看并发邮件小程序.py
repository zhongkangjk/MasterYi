import selenium
import selenium.webdriver
import selenium.webdriver.common.keys
import time
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
import tkinter
import threading
from selenium.webdriver.support.wait import WebDriverWait

_user = ""
_pwd  = ""
_to   = ["@qq.com,@qq.com"]
msg = MIMEMultipart()
msg["Subject"] = "来新单啦"
msg["From"]    = _user
msg["To"]     = ','.join(_to)
def sendemail(word):
    part = MIMEText(word)
    msg.attach(part)
    s = smtplib.SMTP("smtp.163.com", timeout=30)
    s.login(_user, _pwd)
    s.sendmail(_user, msg["To"].split(",") , msg.as_string())
    s.close()
profile=selenium.webdriver.FirefoxOptions()
profile.add_argument('-headless') #设置无头模式
driver = selenium.webdriver.Firefox(options=profile)
driver.implicitly_wait(10)
driver.get("网址")
#elem.click()*-*******
elem = driver.find_element_by_id("userId")
elem.send_keys("登录名")
elem = driver.find_element_by_id("password1")
elem.send_keys("密码")
elem.send_keys(selenium.webdriver.common.keys.Keys.RETURN)
time.sleep(2)
sreach_window=driver.current_window_handle
def open():
	driver.switch_to.frame('FRM_LEFT')
	WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath("""//*[@id="jd3"]"""))
	elem = driver.find_element_by_xpath("""//*[@id="jd3"]""")
	elem.click()
	WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath("""//*[@id="jd16"]"""))
	elem = driver.find_element_by_xpath("""//*[@id="jd16"]""")
	elem.click()
	WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath("""//*[@id="selstr20"]"""))
	elem = driver.find_element_by_xpath("""//*[@id="selstr20"]""")
	elem.click()
	time.sleep(1)
	driver.switch_to.default_content()
	driver.switch_to.frame('FRM_RIGHT')
	try:
		driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div/div[2]/iframe'))
	except:
		driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div/div/iframe'))
	driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="ifrm1"]'))
	driver.find_element_by_xpath("""/html/body/div[2]/form/table/tbody/tr[3]/td[5]/input""").click()
open()
pageSource = driver.page_source
soup = BeautifulSoup(pageSource,"html.parser")
rs = soup.select('#datatable > tbody:nth-child(1)')[0]
list = []
def go(mingzi):
	for n in range(2,41,2):
		name = rs.contents[n].contents[9].string
		if name == mingzi:
			num = rs.contents[n].contents[1].string
			num1 = int(num)+1
			clicknum = '/html/body/div[2]/table/tbody/tr['+str(num1)+']/td[9]/span[2]'
			elem = driver.find_element_by_xpath(clicknum)
			elem.click()
			time.sleep(1)
			名称 = driver.find_element_by_xpath('//*[@id="KHMC"]').get_attribute("value")
			地址 = driver.find_element_by_xpath('//*[@id="DZ"]').get_attribute("value")
			联系人 = driver.find_element_by_xpath('//*[@id="LXRMC"]').get_attribute("value")
			移动电话 = driver.find_element_by_xpath('//*[@id="YDDH"]').get_attribute("value")
			问题 = driver.find_element_by_xpath('//*[@id="wt1"]').text
			list.append([名称,地址,联系人,移动电话,问题])
			driver.find_element_by_xpath('//*[@id="export"]').click()
			time.sleep(1)
			driver.find_element_by_xpath("""/html/body/div[2]/form/table/tbody/tr[3]/td[5]/input""").click()
			time.sleep(1)
def gogo():
	go('名字')
	if list:
		print("有")
		words = '\n' + "接下来看详细报道" + '\n'
		for line in list:
			words += '----'+'\n'
			words += '\n'.join(line)
			words += '\n'
		sendemail(words)
		print()
		text.insert(tkinter.INSERT,"邮件发送成功,浏览器已关闭")
		driver.close()
	else :
		text.insert(tkinter.INSERT,'没有查询到有新的派单\n')
		text.see(tkinter.END)
		#time.sleep(60)
		#driver.refresh()
		#open()
		#gogo()
def gogogo():
	go('名字')
	if list:
		print("有")
		words = '\n' + "接下来看详细报道" + '\n'
		for line in list:
			words += '----'+'\n'
			words += '\n'.join(line)
			words += '\n'
		sendemail(words)
		print()
		text.insert(tkinter.INSERT,"邮件发送成功,浏览器已关闭")
		driver.close()
	else :
		text.insert(tkinter.INSERT,'没有查询到有新的派单\n自动运行中\n')
		text.see(tkinter.END)
		time.sleep(120)
		driver.refresh()
		open()
		gogogo()  #不应该递归  应该定时启动新线程然后取结果关闭就可以了
def thread_it(func, *args):
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()
win = tkinter.Tk()
win.title("检测新单并发送邮件")
win.geometry('250x370+600+300')
tkinter.Button(win,text = "直接检测", command = gogo).pack(fill = "x")
tkinter.Button(win,text = "自动运行", command=lambda :thread_it(gogogo)).pack(fill = "x")
text = tkinter.Text(win,height = 24)
text.pack()
win.resizable(0, 0)#不要动
win.mainloop()




