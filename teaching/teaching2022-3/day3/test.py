import random as rnd

numbers = [i for i in range(1, 46)]
lotto = []

for i in range(6): 
    lotto.append(rnd.choice(numbers))

lotto.sort()
print(f'1등 번호는 {lotto} 입니다.')