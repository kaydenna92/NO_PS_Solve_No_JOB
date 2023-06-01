# 단절점과 단절선 (S1)
# 단절점과 단절선을 트리에서 구하려고 한다. 
# 트리 : 사이클이 존재하지 않으며, 모든 정점이 연결되어 있는 그래프

# 단절점 : 해당 정점을 제거했을 때, 그 정점이 포함된 그래프가 2개 이상으로 나뉘는 경우 
# ->  자식 노드가 하나밖에 없거나, 리프 노드일때, 해당 노드를 제거해도 트리가 2개이상 나뉘지 않음

# 단절선 : 해당 간선을 제거했을 때, 그 간선이 포함된 그래프가 2개 이상으로 나뉘는 경우 
# -> 간선은 노드 2개를 연결하고 있음, 따라서 무조건 yes..


def solution():
    from collections import defaultdict
    import sys
    input = sys.stdin.readline

    n = int(input())
    graph = defaultdict(list)
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    q = int(input()) 
    for _ in range(q):
        a, b = map(int, input().split())

        if a == 1: # b번 정점이 단절점인지에 대한 질의
            if len(graph[b]) < 2:
                print('no')
            else:
                print('yes')

        if a == 2: # b번 간선이 단절선인지에 대한 질의 -> 무조건 yes
            print('yes')

solution()



