import requests
from bs4 import BeautifulSoup
import re
import csv
import datetime
month =['october', 'november' ,'december', 'january', 'february', 'march', 'april', 'may', 'june']
for item in month:
    fh = open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\file\\17-18 ' + item + ' Schedule.csv', 'w', newline='', encoding = 'utf-8')
    writer = csv.writer(fh)    
    URL = 'https://www.basketball-reference.com/leagues/NBA_2018_games-' + item +'.html'
    res = requests.get(URL)
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.thead.find_all('th')
    titlelist = []
    i = 0
    for item in title:
        i += 1
        if i == 2:
            continue
        else:
            titlelist.append(item.text)
        if i == 6:
            writer.writerow(titlelist)
            break
    tbody = soup.tbody.find_all(['a', 'td'])
    tbodylist = []
    j = 0
    for item in tbody:
        j += 1
        if j in [2, 4, 7, 9, 10, 11, 12]:
            continue
        elif j == 13:
            j = 0
            writer.writerow(tbodylist)
            tbodylist = []
        elif j == 1:
            date = datetime.datetime.strptime(item.text, '%a, %b %d, %Y')
            datestr = date.strftime('%Y/%m/%d')
            tbodylist.append(datestr)
        else:
            tbodylist.append(item.text)
    fh.close()