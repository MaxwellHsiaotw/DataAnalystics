import requests
from bs4 import BeautifulSoup
import re
import csv
Team = {'Toronto Raptors': 'TOR', 'Boston Celtics': 'BOS', 'Philadelphia 76ers': 'PHI', 'Cleveland Cavaliers': 'CLE', 'Indiana Pacers': 'IND', 'Miami Heat': 'MIA', 'Milwaukee Bucks': 'MIL', 'Washington Wizards': 'WAS', 'Detroit Pistons': 'DET', 'Charlotte Hornets': 'CHO', 'New York Knicks': 'NYK', 'Brooklyn Nets': 'BRK', 'Chicago Bulls': 'CHI', 'Orlando Magic': 'ORL', 'Atlanta Hawks': 'ATL', 'Houston Rockets': 'HOU', 'Golden State Warriors': 'GSW', 'Portland Trail Blazers': 'POR', 'Oklahoma City Thunder': 'OKC', 'Utah Jazz': 'UTA', 'New Orleans Pelicans': 'NOP', 'San Antonio Spurs': 'SAS', 'Minnesota Timberwolves': 'MIN', 'Denver Nuggets': 'DEN', 'Los Angeles Clippers': 'LAC', 'Los Angeles Lakers': 'LAL', 'Sacramento Kings': 'SAC', 'Dallas Mavericks': 'DAL', 'Memphis Grizzlies': 'MEM', 'Phoenix Suns': 'PHO'}
Month =['october', 'november' ,'december', 'january', 'february', 'march', 'april', 'may', 'june']
AwayTeam = []
HomeTeam = []
fh1 = open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\file\\NBA12manlist.csv', 'w', newline='', encoding = 'utf-8')
writer = csv.writer(fh1)
writer.writerow(['Date', 'Team'])
for month in Month:
    fh = open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\file\\17-18 '+ month +' Schedule.csv', 'r', newline='', encoding = 'utf-8')
    reader = csv.DictReader(fh)
    for row in reader:
        date = row['Date']
        AwayTeam.append(date)
        HomeTeam.append(date)
        datestr = row['Date'].split('/')
        hometeam = Team[row['Home/Neutral']]
        awayteam = Team[row['Visitor/Neutral']]
        AwayTeam.append(awayteam)
        HomeTeam.append(hometeam)
        URL = 'https://www.basketball-reference.com/boxscores/' + datestr[0] + datestr[1] + datestr[2] + '0' + hometeam + '.html'
        res = requests.get(URL)
        soup = BeautifulSoup(res.text, 'html.parser')
        title = soup.find_all('a', href = re.compile('players'))
        count = away = home = 0
        for item in title:
            if item.text == 'Players' and count != 1:
                count += 1
                continue
            elif item.text == 'Players' and count == 1:
                break
            if item.text in AwayTeam:
                away = 1
                continue
            elif away == 0:
                AwayTeam.append(item.text)     
            if item.text in HomeTeam:
                home = 1
                continue
            elif home == 0 and away == 1:
                HomeTeam.append(item.text)
        writer.writerow(AwayTeam)
        writer.writerow(HomeTeam)
        AwayTeam = []
        HomeTeam = []
    fh.close()
fh1.close()
