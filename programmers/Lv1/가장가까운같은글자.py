from collections import defaultdict

def solution(s):
    answer = [0] * len(s)
    count = defaultdict(list)


    for i in range(len(s)):
        if s[i] not in count: # 안에 존재하지 않을때, 
            count[s[i]].append(i)
            answer[i] = -1
        else:  # 존재한다면?
            count[s[i]].append(i)
            answer[i] = count[s[i]][-1] - count[s[i]][-2]


    return answer

solution('foobar')