import sys
from collections import deque

n, k = map(int, input().split())
que = deque([[n, 0]]) # 내 위치, 시간
visited = [n] # 방문처리

while True:
    position, time = que.popleft()
    
    if position == k:# 동생의 위치에 도착하면 break
        print(time)
        break

    if position * 2 >= 0 and position * 2 <= 100000 and position * 2 not in visited: # 순간이동 먼저해야함! 순간이동은 0초이기때문에 바로 순간이동으로 도착하는 경우가 있음.
        visited.append(position * 2)
        que.append([position * 2, time])

    if position - 1 >= 0 and position - 1 <= 100000 and position - 1  not in visited: # x - 1 이동
        visited.append(position - 1)
        que.append([position - 1, time + 1])

    if position + 1 >= 0 and position + 1 <= 100000 and position + 1  not in visited: # x + 1 이동
            visited.append(position + 1)
            que.append([position + 1, time + 1])
    
# 7206