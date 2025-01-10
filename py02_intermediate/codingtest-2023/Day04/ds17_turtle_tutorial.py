# 프랙탈 별 그리기
from turtle import *
setup(width=600, height=600)

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

mainloop()