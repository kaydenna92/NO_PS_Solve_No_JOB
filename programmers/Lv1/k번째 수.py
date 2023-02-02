def solution(array, commands):
    answer = []
    # commands = [i, j, k] # 시작인덱스, 마지막 인덱스, return해야하는 인덱스 
    # 인덱스는 0부터 시작하기 때문에 -1씩 해줘야함.
    # j는 제외
    
    # 문자열 슬라이싱 사용
    temp = []
    for i in range(len(commands)): # 0, 1, 2
        temp = array[commands[i][0] - 1 : commands[i][1]]
        temp.sort()
        answer.append(temp[commands[i][2] - 1])
    return answer