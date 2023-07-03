# 주의
# 1. 배열의 마지막 원소의 다음 원소는 첫 번째 원소가 된다.
#   구름을 d방향으로 s만큼 읻오하는 경우 % 연산을 사용하기
# 2. 물복사 버그, 범위를 넘어가면 예외처리 하기
#   경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니므로, 예외처리
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
moves = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]
cloud = deque(cloud)


def rain(direction, distance):
    global n
    size = len(cloud)
    for _ in range(size):
        x, y = cloud.popleft()
        nx = (x + dx[direction] * distance) % n
        ny = (y + dy[direction] * distance) % n

        if 0 > nx:
            nx += n

        if 0 > ny:
            ny += n

        cloud.append([nx, ny])
        visited[ny][nx] = True
        board[nx][ny] += 1

