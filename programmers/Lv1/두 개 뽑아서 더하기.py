# numbers가 주어진다
# numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return

numbers = [2,1,3,4,1] # result = [2,3,4,5,6,7]
# numbers = [5, 0, 2 7] # result = [2,5,7,9,12]


def solution(numbers):
    answer = []
    combination = []
    
    def combinations(index, selected):
        nonlocal numbers, answer
        
        if len(selected) == 2:
            answer.append(selected[:])
            return
        for i in range(index, len(numbers)):
            combinations(i + 1, selected + [numbers[i]])
            
    combinations(0, [])
    
    for i in range(len(answer)):
        combination.append(sum(answer[i]))
    
    return sorted(list(set(combination)))


def solution2(numbers):
    answer = []
    for i in range(len(numbers)):
        for k in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[k])

    return sorted(set(answer))

print(solution2(numbers))