def solution(k, m, score):
    answer = 0
    score.sort(reverse = True) 
    box_count = int(len(score) / m)
    boxs = []

    for i in range(0, box_count): 
        boxs.append(score[i * m : m * (i + 1)]) 

    for box in boxs:
        minimum = box[-1]
        answer += minimum * len(box)


    for i in sorted(score, reverse=True):
        print(i)
        
    return answer


solution(3, 4, [1,2,3,1,2,3,1])
solution(4, 3, [4,1,2,2,4,4,4,4,1,2,4,2])