# def add(a, b):
#     return a + b

# print(add(12, 4))

# x = 5
# y = 6
# print(add(x, y))

# print(add(6))

def say_hello(name):
    print(f'Hello, {name}')

say_hello('Hugo')

def multi(x, y):
    return x * y

print(multi(x = 8, y = 4))
print(multi(y = 8, x = 4))


def adds(*args):
    result = 0
    for i in args:
        result += i

    return result


print(adds(1, 2, 3, 4))
print(adds(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def calc(option = 'add', *args):
    result = 0
    if option == 'add':
        for i in args:
            result += i

    elif option == 'mul':
        result = 1
        for i in args:
            result *= i
        
    elif option == 'sub':
        num = 0
        result = args[0]
        for i in args:
            num += 1
            if (num == 1): continue
            result -= i

    elif option == 'div':
        num = 0
        result = args[0]
        for i in args:
            num += 1
            if (num == 1): continue
            result /= i
    
    return result


print(calc('add', 1, 2, 3, 4))
print(calc('sub', 10, 3, 2))
print(calc('mul', 4, 3))
print(calc('div', 13, 5))


def mul_and_div(x, y):
    return x*y, x/y

print(type(mul_and_div(10, 5)))
multi_val, divid_val = mul_and_div(10, 5)
print(multi_val)
print(divid_val)


def add(x, y):
    return x + y

print(add(7, 4))

ladd = lambda x, y: x + y
print(ladd(7, 5))
