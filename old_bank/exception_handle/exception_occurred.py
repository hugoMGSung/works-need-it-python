def add (a, b):
    return a + b

def multi (a, b):
    return a * b

def div (a, b):
    return a / b


print('테스트 시작')
x, y = 4, 0
print(f'더하기, {x} + {y} ')
print(f'결과 {add(x, y)}')
print(f'나누기, {x} / {y} ')

try:
    print(f'결과 {div(x, y)}')  # 예외발생 
except ZeroDivisionError as e:
    print(e)


print(f'곱하기, {x} * {y} ')
print(f'결과 {multi(x, y)}')