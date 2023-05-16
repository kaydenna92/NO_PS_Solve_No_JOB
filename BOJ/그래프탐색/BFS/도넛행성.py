from collections import deque


def bfs(y, x, n, m, info):
    que = deque()
    que.append([y, x])
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

    while que:
        now_y, now_x = que.popleft()

# % 연산 : 항상 분모와 기호가 같은 부호로 반환 된다.
# 10 / 2 = 5 의 의미?
# 10 / 2의 의미는 2를 이용해 10을 만들 수 있는 방법에 대한 것
# 10 = 2 + 2 + 2 + 2 + 2, 다시 말해 2가 5개 있어야 10이 만들어 진다.
# 1 / 24 = 24 * 0 + 1 (몫: 0, 나머지: 1)
# -1 / 24 = 24 * (-1) + 23 (몫: -1, 나머지: 23) -> -1을 이용해 24를 만드는 방법
# 따라서,
# print(1 / 24) # 0.04166666666...
# print(1 // 24) # 몫 : 0
# print(1 % 24) # 나머지 : 1
# print(-1 // 24) : 몫 : -1
# print(-1 % 24) : 나머지 23

        for i in range(4):
            ny = (dy[i] + now_y) % n
            nx = (dx[i] + now_x) % m

            if 0 <= ny < n and 0 <= nx < m:
                if info[ny][nx] == 0:
                    info[ny][nx] = 1
                    que.append([ny, nx])


def main():
    n, m = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(n)]
    answer = 0

    for i in range(n):
        for k in range(m):
            if info[i][k] == 0:
                answer += 1
                info[i][k] = 1
                bfs(i, k, n, m, info)

    return answer

print(main())