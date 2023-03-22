from collections import defaultdict
# point ! 회전 초밥 -> 원형 처리 '%' or 'extend(sushis)'를 이용하여 2개를 붙이기

# 입력
n, d, k, c = map(int, input().split())
sushis = [int(input()) for _ in range(n)] 

# variables 
answer = 0 # 최대 초밥 종류 
start, end = 0, 0
eatable = defaultdict(int) 
eatable[c] += 1 # 쿠폰 초밥

# 초기값 설정
while end < k:
    eatable[sushis[end]] += 1 
    end += 1

# sliding window

while start < n:
    answer = max(answer, len(eatable)) # len(dict)는 키의 길이를 반환함

    eatable[sushis[start]] -= 1

    if eatable[sushis[start]] == 0:
        eatable.pop(sushis[start])
    
    eatable[sushis[end % n]] += 1 # 회전(원형연결리스트)때문에 % 연산자로 인덱스 범위 넘어가지 않게 함.

    # 이동
    start += 1
    end += 1

print(answer)


