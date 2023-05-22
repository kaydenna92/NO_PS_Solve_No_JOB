n, m = map(int, input().split())
basket = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    for ball in range(i - 1, j):
        if basket[ball] != 0: # 공이 이미 들어있으면?
            basket[ball] = 0 # 빼고,
            basket[ball] = k # 다시 넣기
        basket[ball] = k
print(*basket)