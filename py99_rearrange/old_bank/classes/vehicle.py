import math

class Car:
    __number = '54라 9538'
    seats = []

    def add_cls_attr(self, seat_num) -> None:
        Car.seats.append(seat_num)

    
    def add_ins_attr(self, seat_num) -> None:
        self.seats.append(seat_num)

    def __init__(self, number) -> None:
        self.seats = []

        tmp_num = number.split(' ')
        if len(tmp_num) != 2:
            raise ValueError('차량번호가 아닙니다')
        elif len(number) < 8 or len(number) > 9:
            raise ValueError('차량번호가 아닙니다')
        
        self.__number = number
        print('__init__')

    def __str__(self) -> str:
        return f'내차 번호는 {self.__number} 입니다.'

    def get_number(self):
        return self.__number


class MotorVehicle:
    # Mother Class
    __name = '자동차'
    __color = '흰색'
    __plate_number = ''
    __product_year = 1990

    def __str__(self) -> str:
        return f'자동차 부모 클래스입니다'

    def run(self) -> str:
        return f'자동차가 달립니다'

    def stop(self) -> str:
        return f'자동차가 멈춥니다'
