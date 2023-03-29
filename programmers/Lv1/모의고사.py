def solution(answers):
    answer = []
    P1 = [1, 2, 3, 4, 5] # 5
    P2 = [2, 1, 2, 3, 2, 4, 2, 5] # 8
    P3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10
    scores = [0, 0, 0] # 1번, 2번, 3번 수포자의 정답 수 Count
    
    for i in range(len(answers)): 
        
        if answers[i] == P1[i % 5]:
            scores[0] += 1
            
        if answers[i] == P2[i % 8]:
            scores[1] += 1
            
        if answers[i] == P3[i % 10]:
            scores[2] += 1
        
    MAX = max(scores)
    person = 0
    for i in range(len(scores)):
        if MAX == scores[i]:
            answer.append(i + 1)
        
    return answer
