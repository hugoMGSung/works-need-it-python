import serial
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

arduino = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=None)

fig = plt.figure()
ax = plt.axes(xlim=(0, 50), ylim=(0, 1100))
line, = ax.plot([], [], lw=1, c='blue', marker='d', ms=2)

max_points = 1100
line, = ax.plot(np.arange(max_points), 
                np.ones(max_points, dtype=np.float)*np.nan, lw=1, c='blue', marker='d', ms=2)

def init():
    return line

def animate(i):
    y = arduino.readline()
    y = y.decode('utf-8')[:-2]
    y = float(y)

    old_y = line.get_ydata()
    new_y = np.r_[old_y[1:], y]
    line.set_ydata(new_y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=20, blit=False)

plt.show()