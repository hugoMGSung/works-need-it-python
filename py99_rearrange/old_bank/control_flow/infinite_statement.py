num = 0

while True:
    print('''처리할 숫자를 입력하세요.
1. 회원입력
2. 회원검색
3. 회원수정
4. 회원삭제
5. 종료

숫자 입력 : ''', end="")
    num = int(input())

    if num == 1:
        print("회원입력")
    elif num == 2:
        print('회원검색')
    elif num == 3:
        print('회원수정')
    elif num == 4:
        print('회원삭제')
    elif num == 5:
        break
    else:
        continue


    