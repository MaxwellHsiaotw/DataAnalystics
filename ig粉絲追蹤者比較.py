import getpass
from bs4 import BeautifulSoup
import re
import time  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

link = input("輸入想要觀察的ig帳號 : ")
a = int(input("輸入追蹤者人數 : "))
b = int(input("輸入追蹤中人數 : "))
act = input("輸入ig帳號 : ")
pwd = getpass.getpass("輸入ig密碼 : ")
a //= 12
b //= 12
#下面黃的是可以把瀏覽器關掉執行的
'''chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)'''

driver = webdriver.Chrome() 
driver.get("https://www.instagram.com/" + link + "/")
driver.find_element_by_css_selector("button._0mzm-.sqdOP.L3NKy").click()
time.sleep(2)
driver.find_element_by_name("username").send_keys(act)
driver.find_element_by_name("password").send_keys(pwd)
driver.find_element_by_name("password").send_keys(Keys.RETURN)
time.sleep(5)

driver.find_element_by_partial_link_text("追蹤者").click()
time.sleep(5)
length = 500
for i in range(0,a):#一次跳12個人          
    js="document.getElementsByClassName('isgrP')[0].scrollTop="+str(length)
    driver.execute_script(js)  
    time.sleep(3)
    length += 1000
soup = BeautifulSoup(driver.page_source, 'html.parser')        
title = soup.body.find_all('a', re.compile('FPmhX notranslate _0imsa'))
Fr = []
for item in title:
    Fr.append(item.text)

driver.find_element_by_css_selector('span.glyphsSpriteX__outline__24__grey_9.u-__7').click()
time.sleep(3)

driver.find_element_by_partial_link_text("追蹤中").click()
time.sleep(5)
length = 500
for i in range(0,b):#一次跳12個人        
    js="document.getElementsByClassName('isgrP')[0].scrollTop="+str(length)
    driver.execute_script(js)  
    time.sleep(3)
    length += 1000
soup = BeautifulSoup(driver.page_source, 'html.parser')        
title = soup.body.find_all('a', re.compile('FPmhX notranslate _0imsa'))
F = []
for item in title:
    F.append(item.text)

F1 = []
for i in range(0, len(F)):
    if F[i] in Fr:
        continue
    else:
        F1.append(F[i])
F1.sort()
for i in F1:
    print(i)

print("-------------------")

Fr1 = []
for i in range(0, len(Fr)):
    if Fr[i] in F:
        continue
    else:
        Fr1.append(Fr[i])
Fr1.sort()
for i in Fr1:
    print(i)
driver.close()
print("Done")