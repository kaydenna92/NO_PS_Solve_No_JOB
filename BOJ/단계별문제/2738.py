# 두 행렬을 더하는 프로그램을 작성하라

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]
answer = [[0] * m for _ in range(n)]


for i in range(n):
    for k in range(m):
        answer[i][k] += (A[i][k] + B[i][k])
    print(*answer[i])

