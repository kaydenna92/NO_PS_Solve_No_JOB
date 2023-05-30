def bfs(start, relationship, visited):
    from collections import deque
    que = deque([[start, 0]])
    while que:
        person, dist = que.popleft() # 이렇게 popleft() 할때는 [[]] 이런 식으로 deque에 넣어주기
        for relation in relationship[person]:
            if not visited[relation]:
                que.append([relation, dist + 1])
                visited[relation] = dist + 1


def main():
    from collections import defaultdict
    import sys
    n = int(input().strip())
    relationship = defaultdict(list)

    while True:
        a, b = map(int, input().split())
        relationship[a].append(b)
        relationship[b].append(a)

        if a == b == -1:
            break

    answer = defaultdict(int)
    for i in range(1, n + 1):
        visited = [0 for _ in range(n + 1)]
        visited[i] = 1
        bfs(i, relationship, visited)
        answer[i] = max(visited) # visited에 다른 회원들과의 가까운 정도가 저장되어 있음 # max 값이 그 사람의 점수

    min_distance = min(answer.values()) # 여기서 최소값을 찾으면 그 사람이 회장의 점수
    candidate = [key for key, value in answer.items() if value == min_distance] # 후보들 찾기
    print(min_distance, len(candidate))
    print(*candidate)

main()

