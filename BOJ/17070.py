# https://velog.io/@eunseokim/BOJ-17070%EB%B2%88-%ED%8C%8C%EC%9D%B4%ED%94%84-%EC%98%AE%EA%B8%B0%EA%B8%B0-1-dp-%ED%92%80%EC%9D%B4-python

def dfs(y, x, pipe_shape):
    global answer, board, n, H, V, D

    if (y, x) == (n-1, n-1):
        answer += 1
        return
    
    if pipe_shape == H or pipe_shape == D: # 파이프의 모양이 가로, 대각선일 때 가로 이동이 가능함.
        if x + 1 < n and board[y][x + 1] == 0: # 범위 체크, 이동 가능 체크
            dfs(y, x + 1, H) # 가로 이동

    if pipe_shape == V or pipe_shape == D: # 파이프의 모양이 세로, 대각선일 때 세로 이동이 가능함.
        if y + 1 < n and board[y + 1][x] == 0: # 범위 체크, 이동 가능 체크
            dfs(y + 1, x, V) # 세로 이동

    if pipe_shape == H or pipe_shape == V or pipe_shape == D: # 대각선 이동은 파이프의 모양에 상관 없이 모두 가능하다.  굳이 필요없음...
        if x + 1 < n and y + 1 < n: # 범위 체크 
            if board[y + 1][x] == 0 and board[y][x + 1] == 0 and board[y + 1][x + 1] == 0: # 대각선으로 이동할때는 3개의 칸이 비어있어야 이동 가능.
                dfs(y + 1, x + 1, D) # 대각선 이동



n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
board[0][0], board[0][1] = 1, 1 # 파이프 초기 설정

H = 1 # 우 
V = 2 # 하 
D = 3 # 우하
answer = 0 # (n, n)에 도착한 경우의 수

dfs(0, 1, H)
print(answer)

