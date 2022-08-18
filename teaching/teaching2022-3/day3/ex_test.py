# 예외처리 테스트
def add(x, y):
    res = x + y
    return res

def sub(x, y):
    res = x - y
    return res

def mul(x, y):
    res = x * y
    return res

def div(a, b):
    res = a / b  #문제야 문제
    return res

def print_hello():
    print('hello')
    # return

print('계산기 시작')
print_hello()
x, y = 4, 1
print(f'더하기 {x} + {y} = {add(x, y)}')
try:
    print(f'나누기 {x} / {y} = {div(x, y)}')
    # print('17' + 3)    
    # print(int('4.0'))    
# except ZeroDivisionError as ex: # ZeroDivisionError 처리
#     print(f'제수에 0을 넣으면 안됩니다. {ex}')
# except TypeError as ex:
#     print('문자열과 수를 더할 수 없습니다.')
except Exception as ex:
    print(f'예외가 발생했습니다 {ex}')
finally:
    print('예외가 발생한구간을 지나갔습니다')

print(f'빼기 {x} - {y} = {sub(x, y)}')
print(f'곱하기 {x} * {y} = {mul(x, y)}')
print('계산기 종료')


