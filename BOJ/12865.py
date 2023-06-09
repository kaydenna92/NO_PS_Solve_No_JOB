import sys
input = sys.stdin.readline


n, k = map(int, input().split())

things = [[0, 0]]
for _ in range(n):
    things.append(list(map(int, input().split())))
memo = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = things[i][0]
        v = things[i][1]

        if j < w: 
            memo[i][j] = memo[i - 1][j] 

        else: 
            memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - w] + v)
        

print(memo[n][k])
