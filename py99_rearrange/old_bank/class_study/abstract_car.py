from abc import *

class AbstractCar(metaclass=ABCMeta):
    __name = '자동차'
    __color = '흰색'
    __plate_number = ''
    __product_year = 1990

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def stop(self):
        pass