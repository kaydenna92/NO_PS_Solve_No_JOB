# 팔이 교차되지 않게 악수를 하기 -> 악수를 하지 못하는 사람이 생길 수도 있다.
# 총 k쌍이 생긴 상황에서 어떤 i, j 에 대해 i번째 쌍이 a대학의 Xi번째, b대학의 Yi번째 학생이 악수를 했고,
# j번째 쌍이 a대학의 Xj번째, b대학의 Yj번째 학생이 악수를 했고, 하면 Xi < Xj 이면 Yi < Yj여야 한다.

n, m, c = map(int, input().split())
personality_a = [] # a대학 성격
personality_b = [] # b대학 성격
satisfaction = [] # 만족도
answer = [[0] * m for _ in range(n)] # A[i] 와 B[j]가 만났을 때 점수 -> answer[i][j]

for i in range(c):
    satisfaction.append(list(map(int, input().split())))
    personality_a = list(map(int, input().split()))
    personality_b = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        answer[i][j] = satisfaction[personality_a[i] - 1][personality_b[j] - 1]

dp = [[0] * m + 1 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-1] + answer[i-1][j-1], dp[i-1][j])

print(dp[-1][-1])