# 길이가 n인 수열이 주어질때, 수열에서 연속한 1개 이상의 수를 뽑았을 때, 같은 수가 여러 번 등장하지 않는 경우의 수를 구하라

# 2중 for문 시간초과

n = int(input())
array = list(map(int, input().split()))

answer = 0
start, end = 0, 0
visited = [False] * 100001

while start < n and end < n:
    if not visited[array[end]]: # end가 가리키는 숫자가 아직 안 나왔으면, 
        visited[array[end]] = True  # 방문 체크
        end += 1 # end 증가
        answer += (end - start) # 조합 개수 저장

    else: # end가 가리키는 숫자가 이미 나온 경우,
        visited[array[start]] = False # 현재의 start값은 안나온 값... false 처리
        start  += 1 # start 증가.

print(answer)


