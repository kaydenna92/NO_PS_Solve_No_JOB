# n + 1개의 I와 n개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 Pn이라고 한다.
# O가 n개 IOIOIOIOI

n = int(input())
m = int(input())
s = input()

index, count, answer = 0, 0, 0 # 위치, OI 개수, 답

while index < m - 1:
    if s[index:index + 3] == 'IOI': # IOI인지 확인
        count += 1 #  카운트 1 증가
        index += 2 # 인덱스 2 증가
        if count == n:
            answer += 1
            count -= 1 

    else:
        index += 1
        count = 0

print(answer)
