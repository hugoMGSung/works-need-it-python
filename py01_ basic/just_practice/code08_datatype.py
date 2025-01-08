# 자료형 예제
None

print(0 == None)
# False

## 숫자형
galaxy_book_pro_360 = 2_190_000
print(galaxy_book_pro_360)
# 2190000
precision_5570 = 3_019.99
print(precision_5570)
# 3019.99

## 타입확인
win = 10
print(type(win))
# <class 'int'>

nokia = 6.1
print(type(nokia))
# <class 'float'>

## 문자열
bruce_eckel = "Life is short, You need Python"
print(bruce_eckel)
# Life is short, You need Python

bruce_eckel2 = 'Life is short.\nYou need Python'
print(bruce_eckel2)
# Life is short.
# You need Python


bruce3 = '''Life is too short.
... You need Python!'''
print(bruce3)
# Life is too short.
# ... You need Python!

print(type(bruce3))
# <class 'str'>

## 불형
print(1 + 1 == 1)
# False
print(1 * 10 == 10)
# True

bl_true = True
bl_false = False
print(bl_true is True)
# True
print(bl_true == True)
# True

print(type(bl_true))
# <class 'bool'>
print(type(bl_false))
# <class 'bool'>

print('-'*20)
# 내장함수 bool()
print(bool(bl_true))
# True
print(bool(bl_false))
# False
print(bool(bruce_eckel))
# True
print(bool(1))
# True
print(bool(0))
# False

## 복합형 리스트
a1 = 1
a2 = 2
a3 = 3
a4 = 4
a5 = 5
a6 = 6
a7 = 7
a8 = 8
a9 = 9
a10 = 10
print(a1, a2)
#(1, 2)
print(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)
#(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# 리스트
b = [1,2,3,4,5,6,7,8,9,10]
print(b)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 추가
arr1 = [1,2,3]
print(bool(arr1))
# True
arr2 = ['Life', 'is', 2, 'short']
print(arr2)
# ['Life', 'is', 2, 'short']
arr3 = [1, 2, [3, 4, 5]]
print(arr3)
# [1, 2, [3, 4, 5]]

print(type(arr3))
# <class 'list'>

# 빈 리스트
arr4 = []
arr4 = list()
print(arr4)
# []


## 튜플
tuple1 = (1, 2, 3, 4)
print(tuple1)
# (1, 2, 3, 4)
print(type(tuple1))
# <class 'tuple'>

## 딕셔너리
spiderman = { 'name' : 'Peter Parker', 'age' : '18', 'weapon' : 'web shooter' }
print(spiderman)
# {'name': 'Peter Parker', 'age': '18', 'weapon': 'web shooter'}

print(spiderman['name'])
# 'Peter Parker'

print(type(spiderman))
# <class 'dict'>

## 집합
set1 = set([1, 2, 3])
print(set1)
# {1, 2, 3}
set2 = set("Hello World")
print(set2)
# {'e', 'd', 'r', 'o', 'W', 'H', 'l', ' '}



