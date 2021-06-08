import requests
from bs4 import BeautifulSoup
import re
import csv
fh = open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\file\\16-17Player_Stats_Advanced.csv', 'w', newline='', encoding = 'utf-8')
writer = csv.writer(fh)
URL = 'https://www.basketball-reference.com/leagues/NBA_2017_advanced.html'
res = requests.get(URL)
soup = BeautifulSoup(res.text, 'html.parser')
title = soup.thead.find_all('th')
titlelist = []
for item in title:
    if item.text in ['Rk', '\xa0']:
        continue
    else:
        titlelist.append(item.text)
writer.writerow(titlelist)
body = soup.tbody.find_all('td')
data = []
i = 0
for item in body:
    i += 1
    if i == 19 or i == 24:
        continue
    elif item.text == '' and i not in [19, 24]:
        data.append(0.0)
    elif i in [1, 2, 4]:
        data.append(item.text)
    else:
        data.append(float(item.text))
    if i == 28:
        writer.writerow(data)
        data = []
        i = 0
fh.close()