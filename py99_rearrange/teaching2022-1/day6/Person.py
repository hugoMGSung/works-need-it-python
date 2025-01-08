# Person.py
# Person 클래스
class Person:
    name = '무명이' # 아직 이름이 없다
    age = 0
    height = 0
    gender = ''
    feetsize = 250
    bloodtype = ''

    # 생성자
    def __init__(self, name, age, height, gender) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender
        print('Person이 생성되었습니다')

    def 소개한다(self) -> None:
        greeting = f'''안녕하세요. 저는 {self.name} 입니다.
        {self.gender}구요. {self.age}살입니다.
        '''
        print(greeting)

    def 먹는다(self, food):
        print(f'{self.name}이(가) {food}을(를) 먹는다')
    
    def 일한다(self, drink):
        print(f'{self.name}이(가) {drink}을(를) 마시면서 일한다')
        

if __name__ == '__main__':
    smg = Person('성명건', 46, 178.3, 'male') # == __init__(self, name, age):
    # smg.name = '성명건'
    # smg.age = 46
    # smg.height = 178.3
    # smg.gender = '남자'
    smg.feetsize = 260
    smg.bloodtype = 'RH+ B'

    smg.소개한다()
    smg.먹는다('본죽')    
    smg.일한다('핫식스')


    