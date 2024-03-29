# 1번 기둥에 n개의 원판이 있고, 3번 기둥으로 옮겨야 할 때,
# 1. 1번 기둥에 위치한 n개의 원판중 위에 있는 n - 1개의 원판을 2번 기둥으로 옮기기
# 2. 1번 기둥에 남아있는 1개의 원판을 3번 기둥으로 옮기기
# 3. 2번 기둥에 남아있는 n-1개의 원판을 3번 기둥으로 옮기기

# 재귀함수로 구현
def hanoi(n, a, b, c): # n개의 원판이 a 기둥에 있을때, c 기둥으로 모두 이동시키는 함수
  if(n == 1): # 원판이 한개면 a -> c 로 옮기고 끝
    print(a, c, sep = " ")

  else:
    hanoi(n-1, a, c, b) # b번 기둥으로 옮기기
    hanoi(1, a, b, c) # a번 기둥에 남아있는 1개의 원판을 c로 옮기기
    hanoi(n-1, b, a, c) # b번 기둥에 남아있는 n-1개의 원판을 c로 옮기기

n = int(input())
print(2**n-1)
if(n <= 20): # 20 이하만 출력
  hanoi(n, 1, 2, 3)

  