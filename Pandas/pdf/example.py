import csv

f = open('C:\data\csv\weather.csv', encoding='CP949')
data = csv.reader(f)
# 1
#for row in data:
#    print(row)
#f.close

#2
header = next(data)
for row in data:
    print(row[3], end=' ,')
f.close