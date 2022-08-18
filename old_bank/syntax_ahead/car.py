class Car:
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color
        
        

myCar = Car("아이오닉", "흰색")
# print(myCar.name, myCar.color)
# print(myCar[0], myCar[1])

from collections import namedtuple

NewCar = namedtuple('NewCar', ['name', 'color'])
yourCar = NewCar('테슬라', '빨간색')
print(yourCar.name, yourCar.color)
print(yourCar[0], yourCar[1])