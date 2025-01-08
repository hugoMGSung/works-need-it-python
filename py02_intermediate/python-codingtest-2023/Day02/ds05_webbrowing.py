# 스택활용
import ds04_stack as st
import webbrowser # 웹브라우저 모듈
import time

st.SIZE = 5
st.stack = [None for _ in range(st.SIZE)]
st.top = -1

if __name__ == '__main__':
    urls = ['www.naver.com', 'www.daum.net', 'www.nate.com', 'www.google.com']

    for url in urls:
        st.push(url)
        webbrowser.open(f'https://{url}')
        print(url, end='-->')
        time.sleep(1) # 1초 대기

    print('방문종료')
    print(st.stack)
    time.sleep(2) # 5초 대기

    while True:
        url = st.pop()
        if url == None:
            break
        webbrowser.open(f'https://{url}')
        print(url, end='-->')
        time.sleep(1)
    
    print('재방문종료')
    print(st.stack)

    input('꺼지지 말고 기다려!!')