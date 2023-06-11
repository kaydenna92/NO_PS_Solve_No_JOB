# S, T가 주어졌을 때, S를 T로 바꾸기

# 연산종류
# 문자열 뒤에 A를 추가한다.
# 문자열 뒤에 B를 추가하고 문자열을 뒤집는다.

# A 
# AB(B 추가) -> BA(뒤집기)
# BAB(B 추가) -> BAB(뒤집기)
# BABA(A 추가) 


# S를 T로 바꾸지말고... T를 S로 바꾸는게 훨 빠름
import sys 


def dfs(t):
    global flag

    if s == t:
        flag = True

    if len(t) == 0: # 종료
        return 

    if t[-1] == 'A': # T의 맨 마지막이 A면 1번 연산을 수행한 것 -> A 제거 후 dfs
        dfs(t[:-1])

    if t[0] == 'B': # T의 첫 번째가 B면 2번 연산을 수행한 것 -> B 제거하고 뒤집은 후에 dfs
        dfs(t[1:][::-1])



s = input()
t = input()
flag = False

dfs(t)
print(1 if flag else 0)