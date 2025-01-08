count = 3

def openBox():
    global count
    print('종이상자를 엽니다. ^^')
    count -= 1
    if count == 0:
        print('반지를 넣고 반환합니다*****')
        return
    
    openBox() # 자기자신을 다시 호출
    print('종이 상자를 닫습니다.')


if __name__ == '__main__':
    openBox()