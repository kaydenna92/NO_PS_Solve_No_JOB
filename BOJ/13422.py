# T = int(input())
#
# for tc in range(T):
#     n, m, k = map(int, input().split())
#     houses = list(map(int, input().split()))
#
#     stolenMoney = sum(houses[0:m])
#     answer = 1 if stolenMoney < k else 0
#
#     start = 0
#     end = m
#
#     if n == m:
#         print(answer)
#         break
#
#     while start < n:
#         stolenMoney -= houses[start]
#         stolenMoney += houses[end % n]
#
#         if stolenMoney < k:
#             answer += 1
#
#         start += 1
#         end += 1
#
#     print(answer)

#??################??????????????????????????????????가뭐가 문제임?
# 연속된 m개의 집에서 돈을 훔치며, k원을 초과한 돈을 훔치지 않는다.

T = int(input())

for tc in range(T):
    n, m, k = map(int, input().split())
    houses = list(map(int, input().split()))

    stolenMoney = 0
    answer = 0
    start = 0
    end = m

    for i in range(end):
        stolenMoney += houses[i]

    if n == m:
        if stolenMoney < k:
            answer = 1
        else:
            answer = 0
    else:
        while start < n:
            if stolenMoney < k: # 훔친 돈이 k원을 초과하는 경우 pass
                answer += 16

            stolenMoney -= houses[start]
            start += 1
            stolenMoney += houses[end % n]
            end += 1

    print(answer)

