def solution(food):
    answer = '0'
    # food 조건에 맞게 가공
    for i in range(1, len(food)):
        if food[i] == 0: # 1개만 있을 경우 사용 x
            pass
        
        if food[i] % 2 != 0: # 홀수일 경우, -1
            food[i] = food[i] - 1

    temp = [0] * sum(food)

    # temp 배열에 배치
    temp[len(temp) // 2] = 0 # 물 배치
    temp_index = 0
    for i in range(1, len(food)):
        while food[i] > 0:
            temp[temp_index], temp[-temp_index - 1] = i, i
            temp_index += 1
            food[i] -= 2

    answer = ''.join(map(str, temp))
    return answer

# 다른 사람 풀이
def solution2(food):
    answer ="0"
    for i in range(len(food)-1, 0,-1):
        c = int(food[i]/2)
        while c>0:
            answer = str(i) + answer + str(i) 
            c -= 1
    return answer