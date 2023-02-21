# 순열 : 서로 다른 n개의 원소를 가진 집합에서 r개를 선택하여 순서대로 배열
# 조합 : 서로 다른 n개의 원소를 가진 집합에서 r개를 선택하여 그룹을 만든다
# 차이점? : 순열은 수를 뽑은 후 순서를 고려해야 하고, 조합은 순서 고려 x

# 내장 패키지 모듈 사용
from itertools import combinations

arr = [1,2,3,4]
print(list(combinations(arr, 3)))
# [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]

# 재귀사용
# 리스트에서 r개를 뽑아 조합을 만든다.
# DFS
nodes = [i for i in range(10)]
r = 3
visited = []

def dfs(index, list):
    if len(list) == r:
        visited.append(list[:])
        return

    for i in range(index, len(nodes)):
        dfs(i + 1, list + [nodes[i]])

dfs(0, [])
print(visited)


nodes = [i for i in range(10)]
r = 6 # r개 뽑아서 조합만들기
visited = [0] * r

def dfs2(level, startWith):
    if level == r:
        print(visited)
        return

    for i in range(startWith, len(nodes)):
        visited[level] = nodes[i]
        dfs(level + 1, i + 1)

dfs2(0, 0)

# 중복조합
from itertools import combinations_with_replacement
n = [i + 1 for i in range(3)]
r = 2

result = list(combinations_with_replacement(n, r))
print(result)


result = []
m = 2
n = 2
def dfs(index, count):
    if count == m:
        print(*result)
        return
    for i in range(index, n):
        result.append(i + 1)
        dfs(i, count + 1)
        result.pop()

dfs(0,0)