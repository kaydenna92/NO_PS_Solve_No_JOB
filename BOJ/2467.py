# 이분탐색
import sys


input = sys.stdin.readline
n = int(input().rstrip())
liquids = list(map(int, input().split()))

l = 0
r = n - 1
answer = float('inf')

for i in range(n - 1):
    start = i + 1
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        temp = liquids[i] + liquids[mid] # 두 용액 섞기

        if abs(temp) < answer: 
            answer = abs(temp)
            l = i
            r = mid

        if temp == 0: 
            break
        elif temp < 0:
            start = mid + 1
        else:
            end = mid - 1

print(liquids[l], liquids[r])