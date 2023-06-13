# 자연수 A를 B번 곱한 수를 C로 나누고, 나머지를 return
import sys


input = sys.stdin.readline
a, b, c = map(int, input().split())
# 거듭제곱의 성질을 이용하기
# 10 ** 10 => (10 ** 5) ** 2 => ((10 ** 2) * 10) **  2 => (((10 ** 1) ** 10) ** 2) ...

# def power(a, b, c):
#     if b % 2 == 0: # 짝수
#         return power(a, b - 1, c) * a
#     elif b == 0: # just 0
#         return 1
#     elif b == 1: # just 1
#         return a
#     else: # b가 홀수일 때,
#         answer = power(a, b // 2, c) 
#         return (answer ** 2) % c
# print(power(a, b, c) % c)


def get_power(a, b, c):
    if b == 1:
        return a % c
    elif b == 0:
        return 1
    else:
        temp = get_power(a, b // 2, c)
        if b % 2 == 0:
            return (temp * temp) % c
        else:
            return (temp * temp * a) % c
        

print(get_power(a, b, c))