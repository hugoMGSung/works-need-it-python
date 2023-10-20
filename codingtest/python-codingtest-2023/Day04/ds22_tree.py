import turtle
import random as r

def drawTree(length, angle):
	if length < 10:
		return
	
	turtle.pensize(length * 0.1)
	turtle.forward(length)
	
	turtle.right(angle)
	drawTree(length * r.uniform(0.5, 0.9), r.randint(10, 50))
	turtle.left(angle * 2)
	drawTree(length * r.uniform(0.5, 0.9), r.randint(10, 50))
	turtle.right(angle)
	
	turtle.pensize(length * 0.1)
	turtle.backward(length)


screen = turtle.Screen()
screen.setup(600, 600)
turtle.speed(0)
turtle.penup()
turtle.setpos(0, -200)
turtle.pendown()
turtle.left(90)

drawTree(100, r.randint(10, 40))

turtle.done()
turtle.mainloop() # Alt + F4