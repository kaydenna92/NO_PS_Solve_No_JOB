# 클러스터 : 여러 컴퓨터를 하나로 묶은 것
# 컴퓨터 수가 많아질 수록, 각각의 성능이 올라갈 수록 향상.

# n대의 컴퓨터, 각각의 성능은 a[i]라는 정수로 평가가능
# 성능을 d만큼 향상시키는데 드는 비용은 d ** 2
# 업그레이드 안해도 되는 컴퓨터도 있지만, 한 컴퓨터에 두 번 이상 업그레이드는 불가
# 예산 B원이 있을 때, 성능이 가장 낮은 컴퓨터의 성능으로 가능한 최대값을 출력하시오

# 최선의 최저 성능을 어떻게 설정하는가? -> 이분법 계산

N, budget = map(int, input().split())
totalComputingPower = list(map(int, input().split())) # 컴퓨팅 파워
answer = 0

# totalComputingPower.sort() # 의미가 없음.
start, end = min(totalComputingPower), 10**18 # 범위 설정, max(totalComputingPower)는 X, budget의 최대 범위로 설정

while start <= end:
    upgradeCost = 0
    mid = (start + end) // 2

    for CP in totalComputingPower:
        if CP < mid: # 업그레이드할 성능보다 작다면, 업그레이드 가능 # 업그레이드 시킬 수 있는 것들은 성능을 모두 끌어올려야 한다.
            upgradeCost += (mid - CP) ** 2 # 비용 계산
        else:
            continue

    if upgradeCost > budget: # 예산을 넘어가면 업그레이드할 성능 - 1
        end = mid - 1

    else: # 예산이 넘어가지 않을때, 업그레이드할 성능 + 1
        start = mid + 1
        answer = mid

    # answer = mid  # 성능을 개선 시킬 여지가 존재
print(answer)
