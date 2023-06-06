# 트리
# 노드 하나를 지웠을 때, 남은 트리에서 리프 노드의 개수를 return

def dfs(tree, index): 
    tree[index] = -2 # 삭제 표시
    for i in range(len(tree)): # tree 탐색
        if index == tree[i]: # 방금 삭제한 인덱스(노드)를 부모 노드로 가지는 노드를 찾아서 재귀
            dfs(tree, i)
    # 재귀가 끝나면 삭제될 노드는 전부 -2


def find_leafnode(tree):
    # not -2 and 다른 노드의 부모 노드도 아닌 원소를 찾을때마다, count += 1 
    cnt = 0
    for i in range(len(tree)): # 모든 tree 노드 탐색
        if tree[i] != -2 and i not in tree:
            cnt += 1
    return cnt

def main():
    N = int(input()) # 노드 갯수
    tree = list(map(int, input().split())) # 0번 노드부터 N - 1번 노드까지, 각 노드의 부모들.
    delete_node = int(input())

    dfs(tree, delete_node)
    answer = find_leafnode(tree)
    print(tree)
    return answer


print(main())