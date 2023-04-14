from collections import defaultdict

def solution(name, yearning, photo):
    answer = [0] * len(photo)
    missyou = defaultdict(list)

    # # key : name, value : yearning로 가지는 dictionary 초기화
    # for i in range(len(name)):
    #     missyou[name[i]] = yearning[i]

    missyou = dict(zip(name, yearning))

    print(missyou)
    # photo의 각 요소를 하나씩 탐색하며, 그리움 점수 누적
    for i in range(len(photo)): 
        for k in range(len(photo[i])):
            
            # 이름이 missyou에 있다면, 점수 누적
            if photo[i][k] in missyou:
                answer[i] += missyou[photo[i][k]] 
                
    return answer


solution(["may", "kein", "kain", "radi"], 
         [5, 10, 1, 3],
         [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]] )