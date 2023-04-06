def solution(k, m, score):
    answer = 0
    score.sort(reverse = True) 
    box_count = int(len(score) / m) # 박스 개수
    boxs = [] # 박스들의 정보

    for i in range(0, box_count): # 박스에 m개의 사과 넣기
        boxs.append(score[i * m : m * (i + 1)]) 

    for box in boxs: # 박스들을 탐색하면서 판매액 누적
        minimum = box[-1]
        answer += minimum * len(box) 
    return answer


solution(3, 4, [1,2,3,1,2,3,1])
solution(4, 3, [4,1,2,2,4,4,4,4,1,2,4,2])