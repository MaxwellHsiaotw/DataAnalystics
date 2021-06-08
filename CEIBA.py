import re
import time  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

ac = 'B04701206'
ps = '555446HAuuNK'

driver = webdriver.Chrome() 
driver.get("https://my.ntu.edu.tw/login.aspx")
driver.find_element_by_name("user").send_keys(ac)
driver.find_element_by_name("pass").send_keys(ps)
driver.find_element_by_name("pass").send_keys(Keys.RETURN)
time.sleep(2)
driver.get("https://ceiba.ntu.edu.tw/")
driver.find_element_by_xpath('//*[@id="obj1"]/form/p/input').click()
time.sleep(5)
link = '#main > table:nth-child(5) > tbody > tr:nth-child(2) > td:nth-child(5)'
i = 2
for i in range(2, 47):
	print(driver.find_element_by_css_selector('#main > table:nth-child(5) > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(5)').text)
for j in range(2, 13):
	print(driver.find_element_by_css_selector('#main > table:nth-child(7) > tbody > tr:nth-child(' + str(j) + ') > td:nth-child(5)').text)
#main > table:nth-child(5) > tbody > tr:nth-child(2) > td:nth-child(5)
#main > table:nth-child(5) > tbody > tr:nth-child(3) > td:nth-child(5)
#main > table:nth-child(7) > tbody > tr:nth-child(2) > td:nth-child(5)
#main > table:nth-child(7) > tbody > tr:nth-child(13) > td:nth-child(5)
#main > table:nth-child(5) > tbody > tr:nth-child(41) > td:nth-child(5)