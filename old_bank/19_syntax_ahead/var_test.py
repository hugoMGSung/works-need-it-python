def foo(*args):
    # [print(i) for i in args]
    print(args)
    
def foofoo(**kargs):
    # print(kargs)
    [print(k, v) for k, v in kargs.items()]
    
foo(1, 2, 3)
foo('나', '집에', '가요')

foofoo(a=1, b=2, c=3)

def times3(x):
    return x * 3

print(times3(9))

v = lambda x : x * 3
print(v(3))