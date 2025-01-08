# exception_handle.py
# 예외처리!! 가장 중요!!!!!!!!!!!!!!!!!!!!!!
def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multi(a, b):
    return a * b

def divide(a, b):
    res = a / b
    return res

print('사칙연산 시작')
a, b = 4, 1
numbers = [3, 6, 9] # 리스트 생성

try:
    print(f'나누기 결과 : {divide(a, b)}')
    res = int(numbers[1]) * 8
    num = int(input('수를 입력하세요'))

except ZeroDivisionError as e:
    print(f'나누기 예외. 추가처리1 {e}')
except IndexError as e:
    print(f'인덱스 예외. 추가처리2 {e}')
except ValueError as e:
    print(f'제발! 쫌 숫자만 넣으라고!!!!!!!!')
except Exception as e:
    print(f'알수없은 예외. 추가처리5 {e}')
finally:
    print(f'곱하기 결과 : {multi(a, b)}')
    print(f'  빼기 결과 : {minus(a, b)}')
    print(f'더하기 결과 : {add(a, b)}')

print('사칙연산 종료')
