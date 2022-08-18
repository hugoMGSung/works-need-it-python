class Fruit(object):
    def __init__(self, name, price):
        self._name = name
        self._price = price
        
    def __add__(self, target):
        return self._price + target._price

    def __sub__(self, target):
        return self._price - target._price

    def __mul__(self, target):
        return self._price * target._price

    def __truediv__(self, target):
        return self._price / target._price
    
def __str__(self) -> str:
    return self._name


strawberry = Fruit("딸기", 10000)
applemango = Fruit("애플망고", 7600)
print(strawberry + applemango)
print(strawberry._price + applemango._price)
print(f'{strawberry}, {applemango}')