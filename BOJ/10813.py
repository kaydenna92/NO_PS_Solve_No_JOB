# 바구니를 총 n개 가지고 있고 바구니는 1번부터 n번까지 번호가 적혀있음
# 바구니에는 공이 1개씩 들어있고, 처음에는 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 들어있음!

# m번 공을 바꾸는데, 공을 바꿀 바구니 2개를 선택하고, 두 바구니에 들어있는 공을 서로 교환
# 공을 어떻게 바꿀지 주어졌을 때, m번 공을 바꾼 이후에 각 바구니에 어떤 공이 들어있는지 구하는 프로그램?

n, m = map(int, input().split())
balls = [i for i in range(1, n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    balls[a - 1], balls[b - 1] = balls[b - 1], balls[a - 1] # swap

print(*balls)

