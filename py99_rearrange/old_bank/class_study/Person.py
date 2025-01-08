import math

class Person:
    count = 0

    def __init__(self, name=None):
        if name is None:
            self.name = '무명이'
        else:
            self.name = name

        Person.count += 1
        print(f'{str(self.name)} 탄생')

    def get_count(self):
        return Person.count
    
    def __str__(self) -> str:
        return f'출력 / 이름은 {self.name} 입니다.'

    def show(self):
        print(f'Name: {str(self.name)}')

# p = Person()
# p.data = 5
# print(type(p))
# print(id(Person))
# print(id(p))
# print(p.data)
p1 = Person()
p1.show()
p2 = Person('명건')
p2.show()

# print(p1.get_count())
# print(Person.count)
print(p2)
