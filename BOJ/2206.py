import sys
from collections import deque


def bfs(y, x):
    q = deque()
    q.append([y, x])

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        y, x, = q.popleft()

        if (y, x) == (n - 1, m- 1): # 가능 return
            return 
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i] # 새 좌표 설정

            if 0 <= ny < n and 0 <= nx < m: # 범위 체크,
                # 벽 X
                if board[ny][nx] == 0:
                    pass
                # 벽 break
                elif board[ny][nx] == 1:
                    pass

            
        return -1 # 불가능
    
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

print(bfs(0, 0))