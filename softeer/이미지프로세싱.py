import sys
from collections import deque
input = sys.stdin.readline
def bfs(y, x, new_color, arr):
    que = deque()
    que.append([y, x])
    past_color = arr[y][x] # 기존 색상 정보 저장
    arr[y][x] = new_color # 시작 위치 색상 변경
    visited = [[False] * W for _ in range(H)]

    # 상 하 좌 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while que:
        py, px = que.popleft()

        for i in range(4):
            ny = dy[i] + py
            nx = dx[i] + px
            
            if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx] and arr[ny][nx] == past_color:
                visited[ny][nx] = True
                arr[ny][nx] = new_color
                que.append([ny, nx])

def print_image():
     for i in range(H):
        for k in range(W):
            print(image[i][k], end = ' ')
        print()

H, W = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())
        
for i in range(Q):
    i, j, c = map(int, input().split())
    bfs(i - 1, j - 1, c, image) # 인덱스 처리(인덱스는 0부터 시작)

print_image()

