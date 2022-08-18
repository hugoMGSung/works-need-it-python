class pycls_custom:

    # 생성자
    def __init__(self, param1, param2):
        self.cus_param1 = param1
        self.cus_param2 = param2

    # 메서드 선언
    def cus_method1(self):
        print('cus_method1 executed')
        pass

    def cus_method2(self):
        print('cus_method2 executed')
        pass


# 메인 코드
# 인스턴스 생성
cls1 = pycls_custom('Hugo', 'Sung')
cls2 = pycls_custom('Asley', 'Park')

# 인스턴스 별 메서드 실행
cls1.cus_method1()
cls1.cus_method2()
cls2.cus_method1()
cls2.cus_method2()