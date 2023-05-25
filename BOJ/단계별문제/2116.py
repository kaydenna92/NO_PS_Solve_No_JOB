n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]
bt_pair = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0
}
result = 0
for i in range(6):
    answer = []
    dice_numbers = [i for i in range(1, 7)]
    bottom = dices[0][i]
    dice_numbers.remove(bottom)
    top = dices[0][bt_pair[i]]
    dice_numbers.remove(top)
    answer.append(max(dice_numbers))

    for k in range(1, n):
        dice_numbers = [i for i in range(1, 7)]
        dice_numbers.remove(top) # 다음 주사위의 아랫면은 이전 주사위의 top
        top = dices[k][bt_pair[dices[k].index(top)]] # 다음 주사위의 윗면 설정
        dice_numbers.remove(top) # 해당 윗면의 숫자 삭제
        answer.append(max(dice_numbers)) # 남은 것들 중에서 제일 큰 숫자 추가

    answer = sum(answer) # 숫자 더하기

    if result < answer: # 모든 경우의 숫자 합의 최대값 갱신
        result = answer

print(result) # 출력