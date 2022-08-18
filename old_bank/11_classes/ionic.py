from vehicle import MotorVehicle

class ionic(MotorVehicle):
    # child class

    def __init__(self, prod_year, plate_num, color = '흰색') -> None:
        super().__init__()

        self.__name = '아이오닉'
        self.__color = color
        self.__plate_number = plate_num
        self.__product_year = prod_year
        print(f'{self.__name} 인스턴스 생성!!')

    def __str__(self) -> str:
        #return super().__str__()
        return f'제차는 {self.__product_year}에 제조한, {self.__color}색의 {self.__name} 입니다.'

    def change_engine(self, mode = '연료') -> None:
        if mode == '연료':
            print('연료로 달립니다')
        elif mode == '전기':
            print('전기로 달립니다. 하이브리드 만쉐!')