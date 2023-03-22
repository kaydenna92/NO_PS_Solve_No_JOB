# 부모 노드 찾기
def find_root(x, parent):
    if parent[x] != x:
        parent[x] = find_root(parent[x], parent)
    
    return parent[x]

def union(node_1, node_2, parent):
    node_1, node_2 = find_root(node_1, parent), find_root(node_2, parent)

    # 작은 루트를 기준으로 union
    if node_1 < node_2:
        parent[node_2] = node_1
    else:
        parent[node_1] = node_2

from collections import Counter
def solution(n, wires): # 노드의 갯수, 간선 정보
    answer = n - 2 # 뭐든 간에 최대값이 된다. 예를 들어 간선의 수가 7개면 6 - 1 : 5개가 최대 차이.

    for wire in wires:
        parent = [i for i in range(n + 1)] # 부모테이블 자기 자신으로 초기화
        cutting_wire = wires[:] # copy
        cutting_wire.remove(wire) # 간선 cutting
        
        # 유니온 연산
        for node1, node2 in cutting_wire:
            if find_root(node1, parent) == find_root(node2, parent): continue # 끊을 송전탑은 union 제외
            union(node1, node2, parent)
        print("처음 유니온하고 난 후 각 노드들의 부모", parent)
        # union 연산 후, 각 노드에 대하여 find_root 연산하여 루트 노드를 확인
        # 0번 때문에 bug 발생!!!!!!!!!!!!!
        # parent 에서 0번 인덱스를 삭제하고 각 노드에 대한 부모를 찾음
        check_root = [] 
        for i in range(1, n + 1):
            check_root.append(find_root(i, parent))
        print("0번 노드 삭제 후 각 노드들의 부모", check_root)
        # Counter를 사용하여 분리된 tree간의 node 갯수를 check
        devided_tree = Counter(check_root)
        devided_tree_value = list(devided_tree.values())
        print("Counter한 값", devided_tree)
        print(" ")

        answer = min(answer, abs(devided_tree_value[0] - devided_tree_value[1]))
    return answer 


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))