# 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다.
# 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다.
# 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하라.

n = int(input())
board = [[0] * 100 for _ in range(100)]

for _ in range(n):
    y, x = map(int, input().split())

    # 검은색 색종이 덮기
    for i in range(10):
        ny = y + i
        board[ny][x] = 1 # y축
        for k in range(10): 
            board[ny][x + k] = 1 # x축

answer = 0
for i in range(100):
    for k in range(100):
        if board[i][k] == 1:
            answer += 1

print(answer)
