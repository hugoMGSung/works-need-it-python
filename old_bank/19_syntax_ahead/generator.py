def bread_gen():
    for i in range(100):
        yield i


g = bread_gen()       # 제너레이터 객체 생성 

bread1 = next(g)
bread2 = next(g)
bread3 = next(g)
print(bread1, bread2, bread3)

bread4 = next(g)
bread5 = next(g)
print(bread4, bread5)