# 프랙탈 그리기
import turtle

turtle.setup(width=600, height=600)

t = turtle.Turtle()  
s = turtle.Screen()  
s.bgcolor("black")  
t.pencolor("red")  
  
a = 0  
b = 0  
t.speed(0)  
t.penup()  
t.goto(0,200)  
t.pendown()  
while(True):  
    t.forward(a)  
    t.right(b)  
    a+=3  
    b+=1  
    if b == 210:  
        break  
    t.hideturtle()  
  
turtle.done()
turtle.mainloop()