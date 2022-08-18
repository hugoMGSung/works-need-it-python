# 변수 라이프스코프
a = 10  # 전역변수

def vartest(a):
    a = a + 1 # 지역변수
    return a

a = vartest(a)
print(a)