'''
tkinter 사용예제 소스
라즈비안 python에 기본 설치되어 있으나 thread safe된(화면 멈추지 않는) 
예제로 하고자 하면 아래의 라이브러리 설치

1. threadsafe_tkinter 설치
pip install threadsafe-tkinter
2. 나머지 작업은 tkinter와 동일
'''
from tkinter import *

root = Tk()
# Label(tk, text='Hello World').pack()
root.title('Event test')
root.geometry('640x400+20+20')

def callback():
    # print('Event 발생!!')
    exit(0)

button = Button(root, text='Quit', \
            width=20, command=callback)
button.pack(padx=10, pady=10)
root.mainloop()
