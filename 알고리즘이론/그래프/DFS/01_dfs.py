
graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A','D','E']
graph['C'] = ['A','C','F']
graph['D'] = ['B']
graph['E'] = ['B']
graph['F'] = ['C']

visited = []
def recursive_dfs(start_node, visited):
    global graph
    visited.append(start_node) # 방문처리

    for node in graph[start_node]: # 방문한 노드의 인접노드들을 탐색한다.
        if node not in visited: # 방문하지 않은 노드이면
            visited = recursive_dfs(node, visited) # 한번 더 재귀로 탐색

    return visited # 누적된 결과로 만들기 위해 visited를 리턴,

print(recursive_dfs('A', visited)) # ['A', 'B', 'D', 'E', 'C', 'F']


def stack_dfs(start_node):
    visited = []
    stack = [start_node] # 'A'

    while stack:
        current_node = stack.pop() # current_node = 
        if current_node not in visited:
            visited.append(current_node)
            for node in graph[current_node]:
                stack.append(node)
    return visited


print(stack_dfs('A')) # ['A', 'C', 'F', 'B', 'E', 'D'] 

# 똑같은 dfs이더라도 순서가 다르다
# 재귀적 dfs는 사전식 순서로 방문하고, stack으로 구현한 dfs는 역순으로 방문함.
# 스택으로 구현 시, 가장 마지막에 삽입된 노드부터 꺼내서 반복하게 되고, 이 경우 인접 노드에서 가장 최근에 담긴 노드, 즉 가장 마지막부터 방문하기 때문.
# 인접노드를 한꺼번에 추가하는 형태이기 때문에 bfs와 헷갈릴 수 있지만 깊이 우선으로 탐색한다는 점에서 dfs가 맞음.

 
