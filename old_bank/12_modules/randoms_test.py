import random

numbers = weight = list(range(1, 46))
lottery = []
random.shuffle(weight)

lottery = random.choices(numbers, weights=weight, k = 6)
    
print(lottery)
