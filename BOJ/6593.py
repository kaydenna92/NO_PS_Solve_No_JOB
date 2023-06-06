from collections import deque
import sys
input = sys.stdin.readline

def bfs(y, x, z):


    dy = [1, -1, 0, 0, 0, 0]
    dx = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    q = deque()
    
    q.append([y, x, z, 0])

    while q:
        now_y, now_x, now_z, minute = q.popleft()

        for i in range(6):
            ny = now_y + dy[i]
            nx = now_x + dx[i]
            nz = now_z + dz[i]

            if 0 <= nz < L and 0 <= ny < R and 0 <= nx < C:
                if building[nz][ny][nx] == 'E':
                    return f'Escaped in {minute + 1} minute(s).'

                if visited[nz][ny][nx] == False and building[nz][ny][nx] == '.':
                    visited[nz][ny][nx] = True
                    q.append([ny, nx, nz, minute + 1])


    return 'Trapped!'


while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break

    building = []
    visited = [[[False] * C for _ in range(R)] for _ in range(L)]

    for i in range(L):
        building.append([list(input()) for _ in range(R)])
        input()



    for l in range(L):
        for r in range(R):
            for c in range(C):
                if building[l][r][c] == 'S':
                    visited[l][r][c] = True
                    print(bfs(r, c, l))