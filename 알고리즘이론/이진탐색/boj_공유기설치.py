# 집 n개가 수직선 위에 있음.
# 각각의 집의 좌표는 X1 ... Xn, 같은 좌표를 가지는 일은 없음.
# 언제나 와이파이를 즐기기 위해 집에 공유기 c개를 설치하려고 한다.
# 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에
# 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
# c개의 공유기를 n개의 집에 적당히 설치해서 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램 작성

# 최소 거리 1, 최대 거리는 끝 집과 첫 집 사이의 거리
# 집들 사이의 거리를 기준으로 이분탐색 실행, 
# 주어진 간격(mid)으로 공유기를 설치했을 때 조건(c개의 공유기를 설치할 수 있는 지)을 만족하는 지 확인.
# 조건을 만족하는 거리들 중에서 최대값을 출력하기
import sys
input = sys.stdin.readline

# 입력
n, c = map(int, input().split())
homes = [int(input()) for _ in range(n)]

# 정렬 
homes = sorted(homes)
start, end = 1, homes[-1] - homes[0]

while start <= end:
    mid = (start + end) // 2
    current = homes[0] 
    installedRouter = 1 
    
    for i in range(1, len(homes)):
        if homes[i] >= current + mid: # 다음 집의 위치가 현재 위치 + 공유기 설치 거리 보다 크면 설치 가능!
            installedRouter += 1 # 공유기 설치
            current = homes[i]  # 현재 위치 갱신
    
    # 설치된 공유기가 c보다 많다면, 설치 거리 넓히기 
    if installedRouter >= c:
        start = mid + 1

    # 아니면 설치 거리 좁히기, 
    else:
        end = mid - 1

print(end)