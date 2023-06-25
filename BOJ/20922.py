# 겹치는 건 싫어

# 같은 원소가 k개 이하로 들어있는 최장 연속 부분 수열의 길이 구하기.
from collections import defaultdict
n, k = map(int, input().split())
numbers = list(map(int, input().split()))

# check = [0] * (n + 1)
check = defaultdict(int)
answer = 0
start, end = 0, 0

# k개 이상 중복이 있는지 검사
while end < n:
    if check[numbers[end]] >= k: # k개 이상이 되면 범위 줄이기
        check[numbers[start]] -= 1 
        start += 1 # 줄이기
    else:
        check[numbers[end]] += 1 # 범위 확장
        end += 1
        answer = max(answer, end - start)  # 최장 연속 부분 수열 길이 갱신

print(answer)