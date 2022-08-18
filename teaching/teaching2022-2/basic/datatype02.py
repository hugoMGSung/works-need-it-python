# 문자열
bruce_eckel = 'Life is short.\n\tYou need Python.'
print(bruce_eckel)

# 여러줄 문자열
multi_line = '''Life is short.
You need Python.
And I need C#, too.
'''
print(multi_line)

# 리스트(배열)
b = [1, 2, 3, 4]

print(b)

b.append(5) # 리스트 맨 마지막 추가
print(b)

b.insert(3, 10) # 원하는 인덱스에 추가
print(b)

b.sort() # 오름차순 정렬
print(b)

b.reverse() # 내림차순 정렬
print(b)

b.remove(10) # 원소 삭제
print(b)

print(type(b))
print(b[2])

## 튜블
c = (1, 2, 3, 4)
print(c)
# c.append(5) # error 튜플에서는 값 추가불가
print(c[2])

## 딕셔너리 key : value 쌍의 집합
spiderman = {
    'name' : '피터 파커',
    'age' : 18,
    'weapon' : '웹슈터',
    'memberOfAvengers' : True
}

print(spiderman)
print(spiderman['name'])
print(spiderman['memberOfAvengers'])






