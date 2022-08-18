import csv

file_name = r'부산광역시_시내버스, 마을버스  노선별 이용 건수_20201231.csv'
dir_name = r'D:/data'

f = open(f'{dir_name}/{file_name}', mode='rt', encoding='cp949')
reader = csv.reader(f, delimiter=',')
next(reader)
for line in reader:
    print(line)

f.close()
