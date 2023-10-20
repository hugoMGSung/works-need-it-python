# 백준 11724 - 연결요소 개수 확인
import sys
# 재귀호출 파이썬 제한 1000번(기본)까지 가능
sys.setrecursionlimit(10 ** 6) # 1000000 
# 입력받는 속도가 느리기때문에, 백준에서 그냥 돌리면 입력오류 발생가능
input = sys.stdin.readline

n, m = map(int, input().split()) # 6 5
A = [[] for _ in range(n+1)] # x, 7열 2차원 리스트
visited = [False] * (n+1) # [0, 1, 2, 3, 4, 5, 6]

# DFS 함수(재귀함수)
def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]: # 방문을 안했다면
            DFS(i)

for _ in range(m): # 에지 개수만큼
    s, e = map(int, input().split())
    A[s].append(e)  # 무방향이기때문에 양쪽 에지 추가
    A[e].append(s)

count = 0

for i in range(1, n+1):
    if not visited[i]: 
        count +=1
        DFS(i)

print(count)