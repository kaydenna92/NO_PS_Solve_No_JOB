# 크루스칼, MST(최소신장트리)
# 플로우 관리비용은 board[i][j]
# i == j인 경우, 0
# 설치비용은 무시
import sys
input = sys.stdin.readline


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
parent = [i for i in range(n)] 
graph = [list(map(int, input().split())) for _ in range(n)] # 플로우 관리비용
edges = [] # 간선 정보 입력할 list

for a in range(n):
    for b in range(a + 1, n):
        edges.append((graph[a][b], a, b)) # 간선정보 입력
 
edges.sort() # 간선정보를 최소 비용순으로 정렬

result = 0

for edge in edges:
    cost, a, b = edge

    if find_parent(a) != find_parent(b): # 같은 집합이 아니면
        union_parent(a, b) # 노드 연결,
        result += cost # + 비용

print(result)