import csv
import datetime
fh = open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\file\\betdata.csv', 'r', newline='', encoding = 'utf-8')
fh1 = open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\file\\result.csv', 'w', newline='', encoding = 'utf-8')
aa = fh.readline()
reader = csv.reader(fh)
writer = csv.writer(fh1)
writer.writerow(['Date', 'AwayTeam', 'HomeTeam', 'CorrectorIncorrect'])
a = 0
temp = []
for row in reader:
    if a == 0:
        temp = row
        a += 1
        continue
    if a == 1:
        aa = float(temp[2].strip())
        bb = float(row[2].strip())
        if aa > bb and temp[3] == 'W':
            writer.writerow([row[0]] + [temp[1]] + [row[1]] + ['Correct'])
            a = 0
            temp = []
            continue
        elif aa > bb and temp[3] == 'L':
            writer.writerow([row[0]] + [temp[1]] + [row[1]] + ['InCorrect'])
            a = 0
            temp = []
            continue
        elif aa < bb and temp[3] == 'W':
            writer.writerow([row[0]] + [temp[1]] + [row[1]] + ['InCorrect'])
            a = 0
            temp = []
            continue
        elif aa < bb and temp[3] == 'L':
            writer.writerow([row[0]] + [temp[1]] + [row[1]] + ['Correct'])
            a = 0
            temp = []
            continue
fh.close()
fh1.close()