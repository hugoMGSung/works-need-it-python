import matplotlib.pyplot as plt
import matplotlib.animation as anim
from collections import deque
import random
 
MAX_X = 100   #width of graph
MAX_Y = 1000  #height of graph
 
line = deque([0.0]*MAX_X, maxlen=MAX_X)
 
def update(fn, l2d):
    dy = random.randint(-5, 5)
    line.append(line[MAX_X-1]+dy)
    l2d.set_data(range(-MAX_X/2, MAX_X/2), line)
 
fig = plt.figure()
a = plt.axes(xlim=(-(MAX_X/2),MAX_X/2), ylim=(-(MAX_Y/2),MAX_Y/2))
l1, = a.plot([], [])
ani = anim.FuncAnimation(fig, update, fargs=(l1,), interval=50)
 
plt.show()