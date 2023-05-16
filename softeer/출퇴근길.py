
import sys
sys.setrecursionlimit(10 ** 6)


def dfs(now, adj, visit):
    if visit[now] == 1: # 방문했으면 종료
        return
    visit[now] = 1 # 방문하지 않은 경우 방문 처리,
    for neighbor in adj[now]: # 해당 노드에 연결된 모든 노드를 탐색
        dfs(neighbor, adj, visit)
    return


def main():
    # 데이터 입력
    node, edge = map(int, input().split())
    graph = [[] for _ in range(node + 1)]
    graph_Reverse = [[] for _ in range(node + 1)]
    for _ in range(edge):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph_Reverse[y].append(x)

    S, T = map(int, input().split())

    fromS = [0] * (node + 1)
    fromS[T] = 1
    dfs(S, graph, fromS)
    fromT = [0] * (node + 1)
    fromT[S] = 1
    dfs(T, graph, fromT)
    toS = [0] * (node + 1)
    dfs(S, graph_Reverse, toS)
    toT = [0] * (node + 1)
    dfs(T, graph_Reverse, toT)

    count = 0
    for i in range(1, node + 1):
        if fromS[i] and fromT[i] and toS[i] and toT[i]:
            count += 1
    print(count - 2)

main()