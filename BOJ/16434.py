# 구현
import sys
input = sys.stdin.readline
import math

n, atk = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
hp, max_hp = 0, 0

for t, a, h in data:
    if t == 1:
        hp += (math.ceil(h / atk) - 1) * a
    
    else:
        max_hp = max(max_hp, hp)
        atk += a
        hp -= h
        if hp < 0:
            hp = 0


print(max(max_hp, hp) + 1)