# n이 1이 될 때까지 아래의 2가지 과정을 거친다
# n에서 1을 빼기
# n을 K로 나누기
# n을 1로 만드는 최소횟수

# 최대한 많이 나누는 것이 최소 횟수를 구하는 것
# n이 k보다 작으면 k로 나누기 X
# 나머지는 -1씩 빼서 구하기

def solution(n, k):
    count = 0
    while n >= k: # n이 k보다 클 경우까지만 실행.
        while n % k != 0 : # 배수가 아니면 1씩 빼고 횟수 증가 # 24를 3으로 나누면 -> 8 -> 7 -> 6 -> 2 -> 
            n -= 1
            count += 1
        n //= k  # 배수면 나누기
        count += 1 # 횟수 증가
    
    while n > 1:
        n -= 1
        count += 1
    return count

print(solution(25, 3))