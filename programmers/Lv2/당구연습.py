
# 원 쿠션으로 이동한 거리를 제곱하여 구하기
# 무조건 공 -> 벽 -> 공 
# 공 -> 공의 경우 제외!!!

# 이동할 수 없는 경우를 제외하여 계산해야 함

# x 좌표가 같을 때
# 상 -> x 좌표가 같고 타겟의 y값이 더 큰 경우,
# 하 -> x 좌표가 같고 타겟의 y값이 작은 경우,

# y좌표가 같을 때,
# 좌 -> y 좌표가 같고, 타겟의 x값이 더 작은 경우,
# 우 -> y 좌표가 같고, 타겟의 x값이 더 큰 경우,

# 다 다른경우!!!!!!!!!!

def solution(m, n, startX, startY, balls):
    answer = []
    startX, startY = x1, y1
    for x2, y2 in balls:
        length = 123913123591350913
        # 상
        if x1 != x2 or y2 > y1:
            length = min(length, (x1 - x2) ** 2 + (y1 + y2) ** 2)
        # 하
        if x1 != x2 or y2 < y1:
            length = min(length, (x1 - x2) ** 2 + (2 * n - y2 - y1) ** 2)
        # 좌
        if y1 != y2 or x2 > x1:
            length = min(length, (x1 + x2) ** 2 + (y1 - y2) ** 2)
        # 우
        if y1 != y2 or x2 < x1:
            length = min(length, (2 * m - x2 - x1) ** 2 + (y1 - y2) ** 2)

        answer.append(length)
    return answer


solution(10, 10, 3, 7, [[7,7], [2, 7], [7, 3]])
