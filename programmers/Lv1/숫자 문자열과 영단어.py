def solution(s):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ''


    temp = ''
    for el in s:
        if el.isdigit():
            answer += el
        else:
            temp += el
            if temp in numbers:
                answer += str(numbers.index(temp))
                temp = ''

    return int(answer)


print(solution("one4fiveseven"))