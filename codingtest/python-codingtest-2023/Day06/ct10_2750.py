# 백준 2750 - 수 정렬하기
N = int(input())
A = [0]*N

for i in range(N):
    A[i] = int(input())

for i in range(N-1):
    for j in range(N-1-i):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]  # 파이썬을 쓰는 이유

for i in range(N):
    print(A[i])