n = int(input())
wine = []
for i in range(n):
    wine.append(int(input()))

d = [0]*n
d[0] = wine[0]

if n > 1:
    d[1] = wine[0]+wine[1]


if n > 2:
    d[2] = max(wine[2]+wine[1], wine[2]+wine[0], d[1])


for i in range(3, n):
    # 현재 포도주를 마실지 말지 결정할 때?
		# 현재 포도주와 이전 포도주를 마시고 전전 포도주는 마시지 않는다 와
		# 현재 포도주와 전전 포도주를 마시고 이전 포도주는 마시지 않는다 와
		# 현재 포도주를 마시지 않는다의 경우로 나뉜다! 
		# 여기서 최대값~
    d[i] = max(d[i-1], d[i-3]+wine[i-1]+wine[i], d[i-2]+wine[i])

print(d[n-1])

# 31256	404ms <--!!!