# * 찍기
for x in range(1, 6):
    for y in range(x, 5):
        print(' ', end='')
    
    for y in range(1, x):
        print('*', end='')

    print('')


print('Hello', end=' ')
print('World')