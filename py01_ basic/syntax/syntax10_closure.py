def calc():
    a = 3
    b = 5
    total = 0
    def firstorder(x):
        nonlocal total
        total = total + a * x + b
        print(total)
    return firstorder
 
c = calc()
c(1)
c(2)
c(3)