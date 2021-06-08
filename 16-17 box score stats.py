import requests
from bs4 import BeautifulSoup
import re
import csv
NBAteam = ['TOR', 'BOS', 'PHI', 'CLE', 'IND', 'MIA', 'MIL', 'WAS', 'DET', 'CHO', 'NYK', 'BRK', 'CHI', 'ORL', 'ATL', 'HOU', 'GSW', 'POR', 'OKC', 'UTA', 'NOP', 'SAS', 'MIN', 'DEN', 'LAC', 'LAL', 'SAC', 'DAL', 'MEM', 'PHO']
fh = open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\file\\16-17player_avg_away.csv', 'w', newline='', encoding = 'utf-8')
writer = csv.writer(fh)
fh1 = open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\file\\16-17player_avg_home.csv', 'w', newline='', encoding = 'utf-8')
writer1 = csv.writer(fh1)
fh2 = open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\file\\16-17player_avg_all.csv', 'w', newline='', encoding = 'utf-8')
writer2 = csv.writer(fh2)
URL = 'https://www.basketball-reference.com/players/l/loveke01/gamelog/2017/'
res = requests.get(URL)
soup = BeautifulSoup(res.text, 'html.parser')
title = soup.thead.find_all('th')
titlelist = []
i = 0
for item in title:
    i += 1
    if item.text == 'Rk':
        titlelist.append('Name')
    elif i in [3, 4, 5, 6, 7, 8, 9, 10, 29, 30]:
        continue
    else:
        titlelist.append(item.text)
writer.writerow(titlelist)
writer1.writerow(titlelist)
writer2.writerow(titlelist)

playerlist = []
for team in NBAteam:
    teamURL = 'https://www.basketball-reference.com/teams/' + team + '/2017.html'
    res = requests.get(teamURL)
    soup = BeautifulSoup(res.text, 'html.parser')
    body = soup.tbody.find_all('a', href = re.compile('players'))
    for player in body:
        if player.text in playerlist:
            break
        link = player.get('href').split('.')
        playerURL = 'https://www.basketball-reference.com' + link[0] + '/gamelog/2017/'
        res = requests.get(playerURL)
        soup = BeautifulSoup(res.text, 'html.parser')
        tbody = soup.tbody.find_all('td')
        tbodylist = []
        awaylist = [0] * 20
        homelist = [0] * 20
        alllist = [0] * 20
        i = j = away = home = all = awayhome = 0
        for item in tbody:
            i += 1
            if i in [1, 2, 3, 4, 6, 7, 9, 28]:
                continue
            elif i == 29:
                i = 0
                continue
            elif i == 8 and item.text not in [ 'Did Not Dress', 'Inactive', 'Did Not Play', 'Player Suspended', 'Not With Team']:
                continue
            elif item.text == '' and i == 5:
                awayhome = 1
                continue
            elif item.text == '@' and i == 5:
                awayhome = 0
                continue
            elif item.text == '' and i != 5:
                tbodylist.append(0)
                continue
            elif item.text == 'Did Not Dress' or item.text == 'Inactive' or item.text == 'Did Not Play' or item.text == 'Player Suspended' or item.text == 'Not With Team':
                tbodylist = []
                i = 0
            else:
                tbodylist.append(float(item.text))
            if i == 27:
                if awayhome == 0:
                    away += 1
                    for a in range(18):
                        awaylist[a + 2] += tbodylist[a]
                elif awayhome == 1:
                    home += 1
                    for a in range(18):
                        homelist[a + 2] += tbodylist[a]
                all += 1
                for b in range(18):
                    alllist[b + 2] += tbodylist[b]
                tbodylist = []
        for a in range(len(alllist)):
            if away != 0:
                awaylist[a] = awaylist[a] / away
            if home != 0:
                homelist[a] /= home
            if all != 0:
                alllist[a] /= all
        awaylist[0] = homelist[0] = alllist[0] = player.text
        awaylist[1] = away
        homelist[1] = home
        alllist[1] = all
        writer.writerow(awaylist)
        writer1.writerow(homelist)
        writer2.writerow(alllist)
        playerlist.append(player.text)
fh.close()
fh1.close()
fh2.close()
print('done')