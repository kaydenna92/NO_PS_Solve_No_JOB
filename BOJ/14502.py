# 바이러스(2)가 퍼지지 않도록 벽(1)을 3개 세울 때, 나머지 안전영역(0)의 최댓값을 return

# bfs
# 벽을 세우는 기준 없이 그냥 모든 경우의 수 탐색하기 -> 백트래킹
# 벽을 세우고, 바이러스 퍼트리고, 안전영역의 최댓값을 찾아서 갱신

def build_wall(cnt):
    if cnt == 3: # 벽 3개 세우면 bfs 실행
        bfs()
        return
    
    for i in range(n):
        for k in range(m):
            if graph[i][k] == 0: 
                graph[i][k] = 1 # 벽 세우기
                build_wall(cnt + 1) # 벽 추가로 세우기
                graph[i][k] = 0 # 벽 허물기


def bfs():
    global graph
    que  = deque()
    temp = copy.deepcopy(graph)

    for i in range(n):
        for k in range(m):
            if temp[i][k] == 2: # 바이러스 넣기
                que.append((i, k))


    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if temp[nx][ny] == 0: # 감염 가능?
                temp[nx][ny] == 2 # 감염
                que.append((nx, ny))

    global answer
    count = 0

    for i in range(n):
        for k in range(m):
            if temp[i][k] == 0:
                count += 1

    answer = max(answer, count)

from collections import deque
import copy, sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer  = 0
build_wall(0)
print(answer)