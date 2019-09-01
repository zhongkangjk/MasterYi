import selenium
import selenium.webdriver
import selenium.webdriver.common.keys
import time

driver = selenium.webdriver.Chrome()
driver.get("http://www.baidu.com")
elem = driver.find_element_by_id("kw")
elem.send_keys(u"鸡翅逗逼")
time.sleep(3)
elem.send_keys(selenium.webdriver.common.keys.Keys.RETURN)


time.sleep(20)
driver.close()