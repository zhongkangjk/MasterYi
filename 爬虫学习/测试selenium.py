#测试代码
from selenium import webdriver
#第一步：创建一个浏览器对象
browser=webdriver.Chrome()
#第二步：使用浏览器对象对网址发起请求
browser.get("https://www.baidu.com")
#获取网页的源代码
print(browser.page_source)
#获取此次请求的地址
print(browser.current_url)
#当前窗口对象
print(browser.current_window_handle)
#获取此次请求的cookie信息
print(browser.get_cookies())
#退出浏览器的命令，注释掉方便我们查看
# browser.quit()
