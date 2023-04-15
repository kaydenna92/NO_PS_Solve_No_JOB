# n X n의 정사각형 공간 위에 a가 있다
# 가장 왼쪽의 좌표는 (1, 1), 가장 오른쪽 아래의 좌표는 (n, n)에 해당한다.
# a는 상 하 좌 우로 이동할 수 있음
# 시작 좌표는 항상 (1, 1)

n = int(input())
moves = list(map(str, input().split()))
move_types = ["L", "R", "U", "D"]
# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# py, px = 0, 0
x, y = 1, 1
for move in moves:
    ny, nx = 0, 0
    for i in range(len(move_types)):
        if move == move_types[i]:
            ny = y + dy[i]
            nx = x + dx[i]

    if 1 <= ny < n and 1 <= nx < n:
        y, x = ny, nx
    else:
        continue

    # if move == "U":
    #     ny, nx = py + dy[0], px + dx[0]
    #
    # elif move == "D":
    #     ny, nx = py + dy[1], px + dx[1]
    #
    # elif move == "L":
    #     ny, nx = py + dy[2], px + dx[2]
    #
    # else:
    #     ny, nx = py + dy[3], px + dx[3]
    #
    # if 0 <= ny < n and 0 <= nx < n:
    #     py, px = ny, nx
    # else:
    #     continue
# print(py + 1, px + 1)
print(x, y)



