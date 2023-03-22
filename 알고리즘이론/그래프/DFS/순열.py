# 순열 : 서로 다른 n개의 원소를 가진 집합에서 r개를 선택하여 순서대로 배열
# 조합 : 서로 다른 n개의 원소를 가진 집합에서 r개를 선택하여 그룹을 만든다
# 차이점? : 순열은 수를 뽑은 후 순서를 고려해야 하고, 조합은 순서 고려 x

import itertools

nodes = ['a', 'b', 'c']
# itertools 라이브러리를 사용하여  순열 구하기 / 가장 빠르고 간단
print(list(map(list, itertools.permutations(nodes))))

# 재귀사용 dfs
# 글로벌 변수 사용 X
def permutation(arr, r):
    arr = sorted(arr)
    used = [False for _ in range(len(arr))]

    def generate(chosen, used):
        if len(chosen) == r: # r개 만큼 선택한 경우 
            print(chosen)
            return
        
        # 모든 노드를 탐색하면서
        for i in range(len(arr)):
            # 아직 사용하지 않았다면?
            if not used[i]:
                # 선택리스트에 저장하고, 방문체크
                chosen.append(arr[i])
                used[i] = True
                # 다시 반복
                generate(chosen, used)
                # 하나의 순열이 만들어지면 uncheck
                used[i] = False
                chosen.pop()

    generate([], used)

permutation(nodes, 2)

# 글로벌 변수 사용 시
def permutation2(arr, r):
    global chosen, used
    if len(chosen) == r:
        print(chosen)
        return

    for i in range(len(arr)):
        if not used[i]:
            chosen.append(arr[i])
            used[i] = True
            permutation2(arr, r)
            used[i] = False
            chosen.pop()

arr = [1, 2, 3, 4]
chosen = []
used = [False for _ in range(len(arr))]

permutation2(arr, 3)

# 전체 순열을 뽑는 경우, r개가 아닌 전체
visited = [False for _ in range(len(nodes))]
answer = []

def dfs(level, list):
    if level == len(nodes):
        answer.append(list[:])
        return

    for index, value in enumerate(nodes):
        if visited[index] == True:
            continue
        
        list.append(value)
        visited[index] = True

        dfs(level + 1, list)
        list.pop()
        visited[index] = False
dfs(0, [])
print(answer) 
# [['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'a', 'c'], ['b', 'c', 'a'], ['c', 'a', 'b'], ['c', 'b', 'a']]

# 중복 순열

from itertools import product
n = [i + 1 for i in range(3)]
r = 2

result = list(product(n, repeat = r))
print(result)

# backtracking

m = 2
result = []
def dfs3(count):
    if count == m:
        print(result)
        return

    for i in range(1, m + 1):
        result.append(i)
        dfs3(count + 1)
        result.pop()
dfs3(0)
