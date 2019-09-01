import selenium
import selenium.webdriver
from selenium.webdriver.chrome.options import Options

# 创建chrome参数对象
opt = selenium.webdriver.ChromeOptions()
# 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
opt.add_argument('-headless')

#url="https://www.youtube.com/results?search_query="+searchname
driver = selenium.webdriver.Chrome(options=opt)
driver.get("https://www.baidu.com")
pagesource=driver.page_source
driver.close()
print(pagesource)




