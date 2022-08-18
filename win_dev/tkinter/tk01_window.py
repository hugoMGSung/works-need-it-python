'''
tkinter 기본GUI 소스
라즈비안 python에 기본 설치되어 있으나 thread safe된(화면 멈추지 않는) 
예제로 하고자 하면 아래의 라이브러리 설치

1. threadsafe_tkinter 설치
pip install threadsafe-tkinter

'''
from tkinter import *

window = None
canvas = None
x1, x2, y1, y2 = None, None, None, None

def mouseClick(event):
	global x1, x2, y1, y2
	x1 = event.x
	y1 = event.y
	
def mouseDrop(event):
	global x1, x2, y1, y2
	x2 = event.x
	y2 = event.y
	canvas.create_line(x1, y1, x2, y2, width = 5, fill = "blue")

window = Tk()
window.title("그림판")
canvas = Canvas(window, height = 480, width = 640)
canvas.bind("<Button-1>", mouseClick)
canvas.bind("<ButtonRelease-1>", mouseDrop)
canvas.pack()

window.mainloop()

