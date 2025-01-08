# 무한루프
num = 0

while True:    
    print('''처리번호를 입력하세요.
1. 회원입력
2. 회원검색
3. 회원수정
4. 회원삭제
5. 종료
입력번호 :''')
    num = int(input()) # 키보드로 입력받은 수를 num할당

    if num == 1:
        print('회원정보입력')
    elif num == 2: # 1은 아니고 2이면
        print('회원검색')
    elif num == 3: # 1, 2도 아니고 3이면
        print('회원수정')
    elif num == 4: # 4라면
        print('회원삭제')
    elif num == 5: 
        print('프로그램종료')
        break
    else:
        print('잘못 입력했습니다')
        continue


