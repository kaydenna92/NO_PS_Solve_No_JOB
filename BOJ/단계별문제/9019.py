 # D, S, L, R
# 레지스터가 존재 0 ~ 10,000 미만의 십진수를 저장할 수 있음

# 각 명령어는 레지스터에 저장된 n을 다음과 같이 변환한다. ((d1 * 10 + d2) * 10 + d3 ) * 10)+ d4
# D : n을 두 배로 바꾼다. 결과 값이 9999보다 큰 경우에는 100000으로 나눈 나머지를 취한다
# S : n에서 1을 뺀 결과를 레지스터에 저장, n이 0이라면, 9999가 저장된다
# L : n의 각 자릿수를 왼편으로 회전,  네 자릿수는 왼편부터 d2, d3, d4, d1
# R : n의 각 자릿수를 오른편으로 회전, 네 자릿수는 d4, d1, d2, d3
 
# 주어진 서로 다른 두 정수 a와 b에 대하여 a를 b로 바꾸는 최소한의 명령어를 생성하는 프로그램을 작성
# a = 1234, b = 3412 일 경우, 두개의 명령어를 적용하면 a를 b로 변환할 수 있다.
# 이때, 출력은 LL 혹은 RR


def D(number): # 입력받은 정수를 두 배로 변환
    temp = number * 2
    if temp > 9999:
        temp = temp % 10000

    return temp


def S(number):
    temp = number
    if temp == 0: return 9999
    temp = temp - 1
    return temp


def L(number):
    # from collections import deque
    # number = str(number)
    # temp = deque([0] * 4)

    # for i in range(len(number)): # 1234 / 123
    #     if len(number) > 3:
    #         temp[i] = number[i]
    #     elif len(number) > 2: # 123
    #         temp[i+1] = number[i]
    #     elif len(number) > 1: # 12
    #         temp[i + 2] = number[i]
    #     else: # 1
    #         temp[i + 3] = number[i]
                
    # left = temp.popleft()
    # temp.append(left)

    # return int(''.join(map(str, temp)))
    first = number % 1000
    end = number // 1000
    temp = first * 10 + end

    return temp

def R(number):
    # from collections import deque
    # number = str(number)
    # temp = deque([0] * 4)

    # for i in range(len(number)): # 1234 / 123
    #     if len(number) > 3:
    #         temp[i] = number[i]
    #     elif len(number) > 2: # 123
    #         temp[i+1] = number[i]
    #     elif len(number) > 1: # 12
    #         temp[i + 2] = number[i]
    #     else: # 1
    #         temp[i + 3] = number[i]
                
    # right = temp.pop()
    # temp.appendleft(right)

    # return int(''.join(map(str, temp)))
    first = number % 10
    end = number // 10
    temp = first * 1000 + end
    return temp

def find(start, target):
    from collections import deque

    que = deque()
    visited = set()
    que.append((start, ''))
    visited.add(start)

    while que:
        current, operation = que.popleft()
        if current == target:
            print(operation)
            return
        
        temp = D(current)
        if temp not in visited:
            visited.add(temp)
            que.append((temp, operation + 'D'))
        
        temp = S(current)
        if temp not in visited:
            visited.add(temp)
            que.append((temp, operation + 'S'))
        
        temp = L(current)
        if temp not in visited:
            visited.add(temp)
            que.append((temp, operation + 'L'))

        temp = R(current)
        if temp not in visited:
            visited.add(temp)
            que.append((temp, operation + 'R'))

        
import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1, T + 1):
    a, b = map(int, input().split())
    find(a, b)
