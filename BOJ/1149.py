N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

# 현재 색 제외, 나머지 두 개의 색의 비용 중 최솟값을 갖고온다
# 각각의 집에 각각의 색을 칠했을 때의 최소비용을 저장함
# 마지막 열 중에서 최솟값이 정답!

for i in range(1, N): # 1번집의 색은 고려 안해도 됨, 아무거나~
    cost[i][0] += min(cost[i-1][1], cost[i-1][2]) # 빨강색, 빨강색 제외 최솟값 찾아서 더하기
    cost[i][1] += min(cost[i-1][0], cost[i-1][2]) # 초록색, 초록색 제외 최솟값 찾아서 더하기
    cost[i][2] += min(cost[i-1][0], cost[i-1][1]) # 파란색, 파란색 제외 최솟값 찾아서 더하기

print(min(cost[-1]))


        


