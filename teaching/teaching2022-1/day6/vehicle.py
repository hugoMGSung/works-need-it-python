# vehicle.py
from typing import overload

class Car:
    차량번호 = '22나 4444'
    __제조사 = '현대'
    색상 = '흰색'
    연료 = '가솔린'
    출고년도 = 2018
    
    def __init__(self, 차량번호, 색상) -> None:
        self.차량번호 = 차량번호
        self.색상 = 색상    
    
    def __str__(self) -> str:
        return f'제차는 {self.출고년도}년에 만들어진 {self.연료} 차량입니다.'

    # private
    def set제조사(self, 제조사):
        self.__제조사 = 제조사

    def 제조사확인(self):
        print(f'제조사 {self.__제조사}')

    def 전진한다(self, level):
        print(f'{self.색상}차가 {level}단으로 앞으로 달린다')

    def 후진한다(self):
        print("뒤로 달린다")

    def 좌회전한다(self):
        print("왼쪽으로 달린다")

    def 우회전한다(self):
        print("오른쪽으로 달린다")

    def 멈춘다(self):
        print("멈춘다")




class Airplane:
    pass