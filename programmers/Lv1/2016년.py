def solution(a, b):
    date = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # day와 month의 차로 계산하여 요일을 얻는다.
    # month의 차이만큼 해당 날을 더하기 위해 1 ~ 12월 까지 month라는 배열을 선언함
    # 차이 계산 후, % 를 사용해 요일을 계산한다.
    diff = b - 1
    for i in range(a - 1):
        diff += month[i]


    return date[diff % 7]


print(solution(5, 24))