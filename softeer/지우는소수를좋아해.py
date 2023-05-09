# 포켓몬 리그에 나가기 위한 최소한의 레벨
# 레벨 x 미만은 도장깨기 x
# 최소한의 레벨이면서 소수인 레벨을 return
# 항상 1번 체육관에서부터 출발하고 마지막 n번 체육관을 지나가야 마지막 포켓몬 리그로 갈 수 있다.

# 다익스트라 알고리즘
# 현재 노드까지 오는데에 필요한 최소 레벨 vs 다음 노드까지 가는데 필요한 레벨의 최댓값 비교
# N번 노드까지 가는데 필요한 레벨보다 크면서, 가장 작은 소수를 구해야 함
# 필요레벨보다 큰 첫번째 소수를 return하기

import sys
import heapq
input = sys.stdin.readline


INF = int(1e9)
n, m = map(int, input().split()) # 노드 개수, 간선 개수
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

weight = [INF for _ in range(n + 1)] # [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF]


def dijkstra(start):
    weight[start] = 0 # 시작 노드는 가중치 0
    heap = [[0, start]] 
    while heap: 
        now = heapq.heappop(heap) 

        if weight[now[1]] < now[0]: # 현재 최소 레벨이 다음 레벨보다 크면 continue
            continue

        for node in graph[now[1]]: 
            next = node[0]
            nextWeight = max(now[0], node[1]) 
            if nextWeight < weight[next]: 
                weight[next] = nextWeight
                heapq.heappush(heap, [nextWeight, next])

dijkstra(1) 
# print(weight)
# 10번노드까지 3레벨이면 통과가 가능하다가 나오니까~

for i in range(weight[n] + 1, weight[n] * 2): # 10번 체육관에 도달하기 위한 최소레벨은 weight[n]임 
    if i % 2 == 0:
        continue

    isPrime = True 
    # 소수 구하기
    for k in range(2, int(i ** 0.5) + 1):
        if i % k == 0:
            isPrime = False
            break

    if isPrime:
        print(i)
        break


