import sys
input = sys.stdin.readline

gearShift = list(map(int, input().split()))
answer = ''

gap = 1
for i in range(1, len(gearShift)):
    if abs(gearShift[i - 1] - gearShift[i]) == gap: # 수열의 차이가 1일때, 
        if gearShift[i - 1] > gearShift[i] : # 앞의 기어가 뒷 기어보다 클 때 내림차순, 
            answer = "descending"
        else: # 아니면 오름차순
            answer = "ascending"
    
    else: # 하나라도 섞여있으면, mixed
        answer = "mixed"
        break
        
print(answer)