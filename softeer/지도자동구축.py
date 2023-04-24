import sys
input = sys.stdin.readline
# 풀이 1
n = int(input()) # 1 <= n <= 15
count = [0] * 16
first = 2
gap = 2

for i in range(1, n + 1):
    first = (first + gap ** (i - 1))
    count[i] = first ** 2

print(count[n])

# import sys
# input = sys.stdin.readline
# 풀이 2
# n = int(input())
# memo = [0] * 16
# memo[0] = 2

# for i in range(1, n+1):
#     memo[i] = memo[i - 1] + (memo[i - 1] - 1)

# print(memo[n] ** 2)

# import sys
# input = sys.stdin.readline
# 풀이 3
# n = int(input())
# count = 2

# for i in range(n):
#     count += (2 ** i)
# print(count ** 2)