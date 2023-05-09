# 1은 장애물, 0은 도로
# 장애물 블록수를 출력하고, 각 블록에 속하는 장애물 수를 오름차순으로 정렬하여 출력하는 프로그램 작성
# 상, 하, 좌, 우, 대각선 제외
# bfs

from collections import deque

def reconize_block(y, x, block, N, visited):
    Q = deque()
    Q.append([y,x])
    visited[y][x] = True
    cnt = 1

    while Q:
        y, x = Q.popleft()

        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]

        for i in range(4):

            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < N: 
                if visited[ny][nx] == False:
                    if block[ny][nx] != 0: 
                        visited[ny][nx] = True
                        Q.append([ny, nx])
                        cnt += 1
    return  cnt

def main():
    N = int(input())
    block = [list(map(int, input())) for _ in range(N)] 
    visited = [[False] * N for _ in range(N)]
    answer = []
    for i in range(N):
        for k in range(N):
            if block[i][k] != 0 and visited[i][k] == 0: # 장애물인데 마주치지 않았을 때, find_block 실행
                answer.append(reconize_block(i, k, block, N, visited))

    answer.sort() 
    print(len(answer)) # 연결된 장애물의 수를 카운트해 append 한 것이므로, 길이가 장애물의 종류 수
    for i in answer:
        print(i)
    
main()
