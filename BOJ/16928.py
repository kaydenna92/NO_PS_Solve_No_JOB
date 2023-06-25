# 뱀과 사다리 게임
# 주사위를 조작해 내가 원하는 수가 나오게 만들 수 있다면, 최소 몇 번만에 도착점에 도착할 수 있는가?
# 도착한 칸이 사다리면, 사다리를 타고 위로 올라간다.
# 뱀이 있는 칸에 도착하면, 뱀을 따라서 내려간다.
# -> 사다리를 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 크다.
# -> 뱀을 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 작음
# 목표 : 최소로 몇 번만에 도착점에 도착하는지 return -> BFS

# 사디리와 뱀 -> 간선이라고 생각함
def bfs(location, count):
    from collections import deque
    q = deque([[location, count]])
    visited[location] = True

    while q:
        node, cnt = q.popleft()

        if node == 100: # 종료 
            print(cnt)
            return
        
        cnt += 1

        for i in range(1, 7): # 주사위
            move = node + i # 이동
            if move > 100 or visited[move]: continue # 100 넘어가거나, 방문한 적이 있으면 continue
            visited[move] = True # 방문처리
            if board[move]: # 사다리 혹은 뱀일 경우, 
                q.append([board[move], cnt])
            else: # 아닐 경우,
                q.append([move, cnt])


n, m = map(int, input().split())
board = [0] * 101
visited = [False] * 101

for _ in range(n + m):
    a, b = map(int, input().split())
    board[a] = b

bfs(1, 0) # 1번부터 탐색