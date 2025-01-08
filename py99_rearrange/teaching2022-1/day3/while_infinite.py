# 무한루프
val = 0

print('회원정보프로그램')
while True:
    print(''' 작업할 번호를 입력하세요.
1. 회원입력
2. 회원검색
3. 회원수정
4. 회원삭제
5. 종료
숫자입력 : ''', end='')
    val = int(input())  # 입력

    if val == 1:
        print('회원정보화면으로 전환')
    elif val == 2:
        print('회원검색화면으로 전환')
    elif val == 3:
        print('회원수정화면으로 전환')
    elif val == 4:
        print('회원삭제화면으로 전환')
    elif val == 5:
        break
    else:
        print('1~5사이의 수를 입력하세요')
        continue


print('회원정보프로그램 종료')