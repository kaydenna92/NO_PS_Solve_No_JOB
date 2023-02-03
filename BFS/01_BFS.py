# 최단 경로를 찾는 다익스타라 알고리즘 등에 매우 유용하게 쓰임.
# 재귀를 이용해 구현을 할 수 없고,
# deque와 queue를 이용해 구현한다.

from collections import deque


visited = []
name = ['A','B','C','D','E','F']
arr = [[0, 1, 1, 0, 0, 0],
       [0, 0, 0, 1, 1, 0],
       [0, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]]

# 큐를 이용한 반복 구조로 구현
def bfs(start_node):
    global visited
    need_visited = deque()
    need_visited.append(start_node)

    while need_visited:
        current_node = need_visited.popleft()
        visited.append(name[current_node])

        for i in range(6):
            if arr[current_node][i] == 1:
                need_visited.append(i)

bfs(0)
print(*visited, sep = ' ')

graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A','D','E']
graph['C'] = ['A','C','F']
graph['D'] = ['B']
graph['E'] = ['B']
graph['F'] = ['C']

def bfs_graph(graph, start_node):
    need_visited, visited = [], []
    need_visited.append(start_node)

    while need_visited:
        current_node = need_visited[0]
        del need_visited[0]

        if current_node not in visited:
            visited.append(current_node)
            need_visited.extend(graph[current_node])

    return visited

print(bfs_graph(graph, 'A'))