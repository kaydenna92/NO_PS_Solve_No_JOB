# 대칭 이동
# 원 쿠션으로 이동한 거리를 제곱하여 구하기

# x가 같을 때,
# 상 하 좌 우 검사
# 벽보다 공을 먼저 때리면 X
# 공 -> 벽 -> 공의 경우만 계산하도록 만들기


# y가 같을 때,
# 위와 동일

# x, y가 모두 다를 때,
# 상 -> x 좌표가 같고 타겟의 y값이 더 큰 경우,
# 하 -> x 좌표가 같고 타겟의 y값이 작은 경우,
# 좌 -> y 좌표가 같고, 타겟의 x값이 더 작은 경우,
# 우 -> y 좌표가 같고, 타겟의 x값이 더 큰 경우,


def solution(m, n, startX, startY, balls):
    answer = []

    for x, y in balls:
        length = 123123123123
        if(x == startX):
            distance1 = (y - startY)
        if (x != startX and y != startY):
            pass

        answer.append(length)
    return answer


solution(10, 10, 3, 7, [[7,7], [2, 7], [7, 3]])
