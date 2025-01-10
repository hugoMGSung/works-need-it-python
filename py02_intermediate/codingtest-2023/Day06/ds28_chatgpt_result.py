import turtle

# 분기 각도와 길이
ANGLE = 30
LENGTH = 80

turtle.setup(width=600, height=600)

def draw_branch(length):
    # 재귀 호출 종료 조건
    if length < 5:
        return
    
    # 왼쪽 가지 그리기
    turtle.forward(length)
    turtle.left(ANGLE)
    draw_branch(length/2)
    
    # 오른쪽 가지 그리기
    turtle.right(2*ANGLE)
    draw_branch(length/2)
    
    # 되돌아오기
    turtle.left(ANGLE)
    turtle.backward(length)

# 초기화
turtle.speed('fastest')
turtle.left(90)

# 재귀 호출 시작
draw_branch(LENGTH)

# 프로그램 종료
turtle.done()
turtle.hideturtle()  
turtle.mainloop()