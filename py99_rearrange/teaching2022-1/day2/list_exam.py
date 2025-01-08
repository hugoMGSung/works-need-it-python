# 리스트 연산
arr = list(range(5))
print(arr)

arr = list(range(1, 6))
print(arr)

arr = list(range(2, 101, 2))
print(arr)

print(arr[0] + arr[5])

# 2차원 배열(리스트)
print()
arr2 = [1, 2, ['Hi', 'My', 'Friend']]
print(arr2[0])
print(arr2[2])
print(arr2[2][1])
print(arr2[2][1][0])

arr3 = list(range(1, 4))
print(arr3)
print(arr3 * 3)
print(arr3 + arr)
print(len(arr))

# 리스트 함수
print('-- 리스트 내장함수')
del(arr3[1])
print(arr3)

arr3.remove(1)
print(arr3)

# 리스트 삭제
arr4 = [4, 2, 6, 9, 12, 16, 7, 1, 3, 3, 5]
arr4.remove(3) # 값을 찾아서 삭제
print(arr4)
del(arr4[8]) # 리스트 인덱스로 삭제
print(arr4)

arr4.sort()
print(arr4)

arr4.reverse()
print(arr4)

arr4.insert(2, 10)
print(arr4)

arr4[0] = 108
print(arr4)

tup1 = tuple(range(1, 6))
print(tup1)
print(tup1[3])

# tup1[0] = 99 # 예외
print(tup1)

# 딕셔너리
dic1 = { 1 : 'a'}
dic1[2] = 'b'
print(dic1)

dic1['name'] = 'Hugo'
print(dic1)

del dic1['name']
print(dic1)

print(dic1.keys())
print(dic1.values())
print(dic1.items())

# 리스트를 튜플 변환
print('-- 리스트/튜플 변환')
print(arr4)
tup2 = tuple(arr4) # 튜플로 변환
print(tup2)

arr4.sort()

print(tup1)
arr5 = list(tup1)
print(arr5)
arr5.append(6)
print(arr5)
tup1 = tuple(arr5)
print(tup1)
