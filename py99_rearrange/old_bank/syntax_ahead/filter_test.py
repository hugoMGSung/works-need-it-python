target = list(range(1, 11))

ret = []
def is_even(n):
    return n % 2 == 0

# for i in target:
#     if is_even(i):
#         ret.append(i)
#ret = list(filter(is_even, target))
ret = list(filter(lambda n : n%2 == 0, target))
        
print(ret)