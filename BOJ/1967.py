# 어떤 두 노드를 선택하여 양쪽으로 당기면, 가장 길게 늘어나느 경우가 있음.
# 이때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게된다.

# 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다.
# 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이 :  트리의 지름

# 설계
# 노드 2개를 선택 (node1, node2)
# 1번 노드에서 가장 먼 노드를 구하기 -> node1
# node1에서 가장 먼 노드를 구하기 -> node2
# node1, node2 사이의 경로의 길이가 트리의 지름


from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

# dfs 탐색
def dfs(start, weight):
    global tree
    for i in tree[start]: # 
        n, w = i
        if distance[n] == -1: # 방문한 적 없으면, 
            distance[n] = weight + w # 가중치 누적
            dfs(n, weight + w) # dfs 재귀

# 입력
n = int(input()) # 노드 개수
tree = defaultdict(list)

# 그래프 입력
for _ in range(n - 1):
    node1, node2, weight = map(int, input().split())
    tree[node1].append([node2, weight])
    tree[node2].append([node1, weight])

# 1번 노드에서 가장 먼 node1 찾기
distance = [-1] * (n + 1) # 노드마다의 가중치를 저장할 배열 선언, 초기값 -1 :  방문 x
distance[1] = 0 # 1번 노드부터 탐색하기 때문에 1번 노드는 0
dfs(1, 0)
# print(distance) # [-1, 0, 3, 2, 8, 13, 11, 9, 15, 28, 17, 17, 21]

# node1에서 가장 먼 node2 찾기
start = distance.index(max(distance)) # node1을 시작 노드로 설정
distance = [-1] * (n + 1) # 초기화
distance[start] = 0
dfs(start, 0)
# print(distance) # [-1, 28, 31, 26, 36, 15, 35, 37, 43, 0, 19, 41, 45]
print(max(distance))
