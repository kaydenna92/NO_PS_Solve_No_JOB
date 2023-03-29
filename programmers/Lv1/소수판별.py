# 1과 자기자신으로만 나누어 떨어지는 수 = 소수

# def solution(n):
#     for i in range(2, n): # 2부터 n - 1 까지의 모든 숫자
#         if n % i == 0: # 나누어 떨어지는게 하나라도 있으면 False
#             return False
        
#     return True # 나누어 떨어지지 않으면 True


# n이 커지면 커질수록 비효율적

# 제곱근까지만 판별하면 더 효율적
# 예를 들어 
# n = 8일때, 약수는?  1, 2, 4, 8

# 약수들이 대칭적으로 짝을 이루어서 8을 완성한다.
# 그렇다면 루트 8은 약 2.8이므로 자연수 2까지만 확인해서 8이 나눠떨어지는 지 확인하면 ok.

# 1 * 8
# 2 * 4
# 4 * 2
# 8 * 1

import math
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if (check_prime(i)) :
            answer += 1
    return answer

def check_prime(number):
    for i in range(2, int(math.sqrt(number))+ 1):
        if number % i == 0:
            return False
    return True


solution(8)