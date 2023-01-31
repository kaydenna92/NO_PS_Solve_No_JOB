def solution(n, arr1, arr2):
    answer = []
    convert = []
    
    def decimal_To_binary(length, number):
        temp = [0] * length
        index = 0

        while number > 0:
            remain = number % 2
            number = number // 2 
            temp[index] = remain
            index += 1
        return ''.join(map(str, (temp[::-1])))
    
    
    for i in range(n):
        convert.append([decimal_To_binary(n, arr1[i]), decimal_To_binary(n, arr2[i])])

    for i in range(len(convert)):
        temp = ''
        for k in range(1, len(convert[i])):
            for j in range(n):          
                if int(convert[i][k-1][j]) == 0: # 0일때만 비교
                    if int(convert[i][k][j]) == 0: # 0이면 빈칸
                        temp += ' '
                    else:
                        temp += '#'       
                else:
                    temp += '#'
        answer.append(temp)

    return answer