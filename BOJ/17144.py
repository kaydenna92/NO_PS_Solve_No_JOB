
def diffusion(board:list, range_y:int, range_x:int):


    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    temp = [[0] * range_x for _ in range(range_y)]


    for y in range(range_y):
        for x in range(range_x):
            diffusion_amount = int(board[y][x] / 5)

            if board[y][x] == 0 or board[y][x] == -1: continue # 이미 0이거나, 공기청정기면 제외
            for d in range(4):

                ny = dy[d] + y
                nx = dx[d] + x

                if 0 <= ny < range_y and 0 <= nx < range_x:
                    if board[ny][nx] >= 0:

                        temp[ny][nx] += diffusion_amount
                        temp[y][x] -= diffusion_amount


    for y in range(range_y):
        for x in range(range_x):
            board[y][x] += temp[y][x]



def purified_air(mode:str, up: int, down: int,range_y:int, range_x:int, array:list):


    if mode == "clockwise":
        dx, dy = (0, -1, 0, 1), (1, 0, -1, 0)
        x, y, d = up, 1, 0
        prev = 0

        while True:
            nx, ny = x + dx[d], y + dy[d] # 이동

            if x == up and y == 0: # 종료 조건(처음 위치로 되돌아온 경우)
                break

            if not 0 <= nx < range_y or not 0 <= ny < range_x:
                d += 1 # 방향 변경
                continue

            array[x][y], prev = prev, array[x][y] # swap
            x, y = nx, ny # 좌표 변경

                
    if mode == "counter_clockwise":
        dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
        x, y, d = down, 1, 0
        prev = 0

        while True:
            nx, ny = x + dx[d], y + dy[d] # 이동

            if x == down and y == 0: # 종료 조건(처음 위치로 되돌아온 경우)
                break

            if not 0 <= nx < range_y or not 0 <= ny < range_x:
                d += 1 # 방향 변경
                continue

            array[x][y], prev = prev, array[x][y] # swap
            x, y = nx, ny # 좌표 변경

        



# 실행(입력 및 함수 호출)
def main():


    r, c, t = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(r)]
    
    for i in range(r):
        if board[i][0] == -1:
            up = i # 위쪽 공청기
            down = i + 1 # 아래 공청기
            break

    for _ in range(t): # t초마다 반복
        diffusion(board, r, c)
        purified_air("clockwise", up, down, r, c, board)
        purified_air("counter_clockwise",up, down, r, c, board)


    answer = 0
    for y in range(r):
        for x in range(c):
            answer += board[y][x]


    return answer + 2 # 공청기 -1 인거 더해주기

    # return (sum(map(sum, board)) + 2)
print(main())