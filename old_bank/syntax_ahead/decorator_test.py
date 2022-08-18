def deco(f):
    def wrapper():
        print("-" * 20)
        f()
        print("-" * 20)
    return wrapper

@deco
def inner():
    print("inner function is called")

deco_inner = deco(inner)
deco_inner()

inner()