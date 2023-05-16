# 4, 345, 23456, 1234567, 0123456789
n = int(input())
for i in range(1, n):
    print(' ' * (n - i) + '*' * (2 * i - 1))

for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

