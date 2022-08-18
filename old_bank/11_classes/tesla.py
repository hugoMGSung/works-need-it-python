from abstract_car import AbstractCar

class tesla(AbstractCar):
    def run(self):
        print('테슬라가 달립니다.')

    def stop(self):
        print('테슬라가 멈춥니다.')