# 가장 긴 바이토닉 부분 수열
# 수열 S가 어떤 수 S[k]를 기준으로 S1 < S2 < S3 < ... < S[k-1] < S[k] > S[k+1] > ... S[n - 1]>  S[n]을 만족하는 수열

# 가장 긴 증가하는 부분 수열 + 가장 긴 감소하는 부분수열 : 가장 최대 길이가 되는 수열의 길이를 return

# 증가하는 부분 수열 조건.
# 1. 자기보다 이전에 있는 원소들 중에서 더 작은 원소 찾기
# 2. 해당 원소를 선택했을 때, 현재 수열의 크기보다 1만큼 더 커지면 값 갱신

# 감소하는 부분 수열 조건.
# 증가하는 부분 수열 조건의 반대

import sys


input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

# 어떤 부분수열이든 초기의 길이는 1
increase = [1] * n 
decrease = [1] * n

# 증가하는 부분 수열
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            increase[i] = max(increase[i], increase[j] + 1)

# 감소하는 부분 수열(역방향)
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if arr[i] > arr[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

result = [0] * n
# 가장 긴 증가하는 부분 수열의 길이 + 가장 긴 감소하는 부분 수열의 길이 - 1 : -1은 S[k]가 중복되므로,
for i in range(n):
    result[i] = increase[i] + decrease[i] - 1

print(max(result))