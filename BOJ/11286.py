import sys, heapq


input = sys.stdin.readline
numbers = []
n = int(input())

for _ in range(n):
    number = int(input())
    if number:
        heapq.heappush(numbers, (abs(number), number)) # 절대값과 입력 받은 수를 튜플로 push
    else:
        if numbers:
            print(heapq.heappop(numbers)[1])
        else:
            print(0)