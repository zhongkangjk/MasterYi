import selenium
import selenium.webdriver
import selenium.webdriver.common.keys
import time

driver = selenium.webdriver.Chrome()
driver.get("https://passport.csdn.net/login?code=public")
elem = driver.find_element_by_xpath('''//*[@id="app"]/div/div/div[1]/div[2]/div[5]/ul/li[2]''')
elem.click()
elem = driver.find_element_by_id("all")
elem.send_keys("name")
time.sleep(3)
elem = driver.find_element_by_id("password-number")
elem.send_keys("password")
time.sleep(3)
elem.send_keys(selenium.webdriver.common.keys.Keys.RETURN)
print(driver.page_source)
time.sleep(20)
driver.close()

#滑块验证没有解决