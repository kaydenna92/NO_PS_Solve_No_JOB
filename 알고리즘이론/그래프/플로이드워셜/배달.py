# import heapq

# def solution(N, road, K):
#     INF = int(1e9)
#     graph = [[] for _ in range(N+1)]
#     distance = [INF] * (N+1)
    
#     for r in road:
#         a, b, c = r
#         # 양방향
#         graph[a].append((b,c))
#         graph[b].append((a,c))
    
#     # 다익스트라 알고리즘 
#     def dijkstra(start):
#         q = []
#         distance[start] = 0
#         heapq.heappush(q, (0, start))
        
#         while q:
#             # 최단거리 노드
#             dist, now = heapq.heappop(q)
#             # 이미 방문했거나 최솟값이 아닌 경우 
#             if distance[now] < dist:
#                 continue 
#             # 연결된 노드들에 대해 
#             for i in graph[now]:
#                 cost = dist + i[1]
#                 # 현재 정보보다 더 적은 시간이 필요한 경우 갱신
#                 if cost < distance[i[0]]:
#                     distance[i[0]] = cost
#                     heapq.heappush(q, (cost, i[0]))
    
#     dijkstra(start=1)
    
#     # K 이하의 시간에 배달이 가능한 마을의 개수 
#     return len([d for d in distance if d <= K])

def solution(N, road, K):
    graph = [[int(1e9) for _ in range(N+1)] for _ in range(N + 1)]

    # self -> self = 0
    for i in range(1, N+1):
        graph[i][i] = 0

    # 양방향 
    for i, j, c in road:
        graph[i][j] = min(graph[i][j], c)
        graph[j][i] = min(graph[j][i], c)

    # 플로이드 워셜
    # k: 반드시 거쳐 지나가는 노드, i: 출발, j: 도착 
    for k in range(1, N+1):    
        for i in range(1, N+1):
            for j in range(1, N+1):
                # i->j 최단 거리: 기존값(graph[i][j])과 k를 지나가는 값(graph[i][k] + graph[k][j]) 중에 더 작은 값
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # 1번 노드에서 각 노드에 도달하는 비용이 K보다 작거나 같은 것만 골라내기
    ans = [distance for distance in graph[1] if distance <= K]
    return len(ans)