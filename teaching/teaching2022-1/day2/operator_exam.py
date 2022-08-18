# 연산자 - 사칙연산
a = 11
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

# 문자열 연산
stat1 = 'Hello'
stat2 = 'World'
res = stat1 + stat2
print(res)
res = stat1, stat2
print(res)

# 문자열연산에서는 +, * 만 있음
print(stat1 + stat2)
# print(stat1 - stat2) # 문자열엔 빼기 없음
print(stat1 * 5)
# print(stat1 * stat2) # 문자열끼리 곱하기 없음
# print(stat1 / 3) # 문자열 나누기 없음

# 문자열 길이
print(len(stat1))
stat3 = '안녕하세요'
print(len(stat3))

# 문자열 인덱스, 리스트와 동일한 작업
# print(stat3[0])
# print(stat3[1])
# print(stat3[2])
# print(stat3[3])
# print(stat3[4])
# print(stat3[5]) ## 예외발생

#stat3[0] = '저'
#stat3[1] = '리'
#print(stat3)

print(stat3[-1])
print(stat3[-2])
print(stat3[-3])
print(stat3[-4])
print(stat3[-5])

# 문자열 자르기
일시 = '2022-01-17 14:39:25'

print(일시[:4], '년')
print(일시[5:7], '월')
print(일시[8:10], '일')
print(일시[11:13], '시')
print(일시[14:16], '분')
print(일시[17:], '초')

print(일시[-5:-3], '분')

list_a = [1,2,3,4,5]
list_a[1] = 19
print(list_a)

print(stat3)
stat4 = '저리가' + stat3[3:]
print(stat4)

## 문자열포맷팅
첫번째 = '투'
두번째 = '유'
str1 = "I'm so happy {0} U. are {1}?".format(첫번째, 두번째)
print(str1)

str2 = f"I'm so happy {첫번째} U. are {두번째}?"
print(str2)

## 숫자 천단위 콤마
money = 10000000000000000
print(format(money, ',d'))

from datetime import datetime

now = datetime.now()  # 현재일시 생성
print(now)
print(now.strftime('%Y년 %m월 %d일 %H:%M:%S'))

import math

myPi = math.pi
print(myPi)

print('{0}'.format(myPi))
print('{0:0.2f}'.format(myPi))
print(f'{myPi:0.6f}')

full_name = 'Hugo MG Sung'
age = 47
greeting = f'''안녕하세요. 저는 {full_name}입니다. 
나이는 {age:0.1f}살 이구요.'''

print(greeting)

part_name = full_name.split()
print(type(part_name))
print(part_name)

test = 'Hey, guys'
print(test.split(','))

# | split
code = 'TEST|2022|01|17|F45678'
split_codes = code.split('|')
print(split_codes)

# 단어교체 replace
print(full_name.replace('Hugo MG', 'Ashley'))

# strip == Oracle TRIM과 동일
aaa = '    Hello, world     '
print(aaa.lstrip())
print(aaa.rstrip())
print(aaa.strip())

print(full_name.index('H'))  # 0
print(full_name.index('u'))  # 1
print(full_name.index('g'))  # 2
print(full_name.index('G'))  # 6
# print(full_name.index('X'))  

print(full_name.find('X'))  # -1
print(full_name.find('MG'))  # 5

print(full_name.count('u'))
print(full_name.count('ng'))

print('-'.join(full_name))

print(full_name.upper())
print(full_name.lower())

 




