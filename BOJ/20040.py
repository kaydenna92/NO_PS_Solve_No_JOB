import sys
input = sys.stdin.readline

def find_root(node):
		# 루트 노드 찾아 삼만리.
    if parents[node] != node:
        parents[node] = find_root(parents[node])
    return parents[node]

def union(node_1, node_2):
    a = find_root(node_1)
    b = find_root(node_2)

		# 부모 테이블 갱신
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

n, m = map(int, input().split()) # 노드 갯수, 수행한 횟수
parents = [i for i in range(0, n)] # 루트 노드 테이블 초기화

# m번 이상 수행 했지만 cycle이 없으면 0, 있으면 i + 1 출력
for i in range(m):  
    node1, node2 = map(int, input().split())
    if find_root(node1) == find_root(node2): # 부모노드가 같다면! -> 사이클이  
        print(i + 1) # 횟수이므로 +1
        break
    else:
        union(node1, node2)
# for문이 끝까지 수행될 경우 수행 : for - else 문법
else:
    print(0)