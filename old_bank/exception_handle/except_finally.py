a = [10, 20, 30, 40]

try:
    index, x = map(int, input('나눌 수를 입력하세요 : ').split())
    y = a[index] / x
    print(y)
except ZeroDivisionError as ze:
    print(f'수를 0으로 나누려고 했습니다.')
except IndexError as ie:
    print(f'인덱스를 잘못입력했습니다. {ie}')
except Exception as e:
    print(f'이외의 예외가 발생했습니다. {e}')
finally:
    print('모든 프로그램을 마쳤습니다.')