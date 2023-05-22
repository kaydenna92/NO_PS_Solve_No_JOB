from collections import deque

que = deque([[1, 2]])
a, b = que.popleft()
print(a, b)