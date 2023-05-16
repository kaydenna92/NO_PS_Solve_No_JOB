n, k = map(int, input().split())
yaksu = []

for i in range(1, n + 1):
    if n % i == 0:
        yaksu.append(i)

if len(yaksu) < k:
    print(0)
else:
    print(yaksu[k - 1])