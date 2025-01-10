# 프로그래머스 템플릿 소스
# 코딩테스트 입문 / 
def solution(numbers):
    numbers = sorted(numbers, reverse=True)
    answer = numbers[0] * numbers[1]    

    return answer

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    print(solution(numbers))

    numbers = [0, 31, 24, 10, 1, 9]
    print(solution(numbers))