# 
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
A = [0] * int(N + 1)

for i in range(1, N+1):
    A[i] = int(input())

A.sort()

for i in range(1, N+1):
    print(str(A[i]) + '\n')