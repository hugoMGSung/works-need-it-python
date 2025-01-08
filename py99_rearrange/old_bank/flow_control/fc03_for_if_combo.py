vals = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

num = 0
for item in vals:
    num += 1
    if num % 2 == 0:
        break
    else:
        print(f'{num}번 수는 {item} 입니다')
