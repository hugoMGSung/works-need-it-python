target = list(range(1, 6))

def add_1(n):
    return n + 1

# ret = []
# for i in target:
#     ret.append(add_1(i))
#ret = list(map(add_1, target))
ret = list(map(lambda n: n+1, target))
    
print(ret)