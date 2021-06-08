import getpass
from bs4 import BeautifulSoup
import re
import time  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pynput.mouse import Controller, Button
mouse = Controller()

link = input("輸入想要觀察的ig帳號 : ")
act = input("輸入ig帳號 : ")
pwd = getpass.getpass("輸入ig密碼 : ")
a = int(input("輸入貼文為第幾篇貼文 : "))
b = int(input("輸入粉絲數共有多少人 : "))
             
q = a % 3
if q == 0:
    count = a // 3
else:
    count = a // 3 + 1
a //= 12             
b //= 12

#下面灰色的是可以把瀏覽器關掉執行的
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

l = 100000
for i in range(0,a): #一次跳12個貼文，可以依需求調整      
    js1="document.documentElement.scrollTop="+str(l)
    driver.execute_script(js1)  
    time.sleep(3) 
    l += l

PostContainerElement = driver.find_element_by_class_name("_2z6nI")
Rows = driver.find_elements_by_class_name("Nnq7C")
nb = 1
for row in Rows:
    if nb < count:
        nb += 1
        continue
    else:
        Boxs = row.find_elements_by_xpath("div")
        for box in Boxs:
            if q == 2:
                q -= 1
                continue
            elif q == 0 :
                q += 2
                continue
            else:
                box.click()
                time.sleep(2)
                a = driver.find_element_by_class_name("Nm9Fw")
                a.find_element_by_class_name("_0mzm-").click()
                time.sleep(5)               
                (mouse.position) = (720, 277)
                mouse.press(Button.left)
                mouse.release(Button.left)
                #time.sleep(5) 
                for i in range(0,3):#一次跳12個粉絲，可以依需求調整  
                    mouse.scroll(0, -1000)        
                    time.sleep(3)
                soup = BeautifulSoup(driver.page_source, 'html.parser')                       
                title = soup.body.find_all('div',' Igw0E rBNOH eGOV_ ybXk5 _4EzTm ') 
                print(title)
                
                count = 0      
                for item in title:
                    if item.text == "":
                        continue
                    else:
                        print(item.text)
                        count += 1
                print("-------------------")
                
                driver.close()
                break
        break
print(count)
print("Done")