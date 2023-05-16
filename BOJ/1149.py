# N개의 집
# 1 ~ N

# 빨강, 초록, 파랑 중 하나의 색으로 칠해야한다.
# 각각의 집을 해당 색으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 return
# 규칙 1. 1번 집의 색은 2번 집의 색과 같지 않아야한다.
# n번 집의 색은 n-1번 집의 색과 같지 않아야한다.
# i (2 <= i <= N-1) 번 집의 색은 i-1번 i+1번 집의 색과 같지 않아야한다.


N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

# 현재 색 제외, 나머지 두 개의 색의 비용 중 최솟값을 갖고온다

for i in range(1, N):
    cost[i][0] += min(cost[i-1][1], cost[i-1][2]) # R
    cost[i][1] += min(cost[i-1][0], cost[i-1][2]) # G
    cost[i][2] += min(cost[i-1][0], cost[i-1][1]) # B

    print(cost)
print(min(cost[-1]))


        


