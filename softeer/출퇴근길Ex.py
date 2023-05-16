from sys import stdin

def to_int(): return map(int, stdin.readline().rstrip().split())

N, M = to_int()
path = [[[] for _ in range(N+1)] for _ in range(2)]
for _ in range(M):
    start, end = to_int()
    path[0][start].append(end)
    path[1][end].append(start)

S, T = to_int()

def move(*nodes):
    from collections import deque
    visited = [set(nodes) for _ in range(2)]
    q = deque()
    for i in range(2):
        q.append(nodes[i])
        while q:
            node = q.popleft()
            for next_node in path[i][node]:
                if next_node not in visited[i]:
                    q.append(next_node)
                    visited[i].add(next_node)

    return visited[0] & visited[1]

s_to_t = move(S, T)
t_to_s = move(T, S)
# print(s_to_t, t_to_s, s_to_t & t_to_s)
print(len(s_to_t & t_to_s) - 2)