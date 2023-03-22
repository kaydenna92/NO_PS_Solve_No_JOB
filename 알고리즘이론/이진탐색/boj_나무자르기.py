
# m을 딱 맞추면 높이의 최대값이 될 듯.


n, m  = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)
answer = 0

while start <= end:
    mid = (start + end) // 2 
    cut_total = 0 # 잘린 나무의 합

    for tree in trees: # trees를 탐색하면서, 
        if tree > mid: # 각각의 tree가 mid보다 크면 cut
            cut_total += tree - mid 
    
    if cut_total >= m: # 원하는 것보다 많이 cut 하면,
        start = mid + 1 # h 증가 
    else: # 원하는 것보다 적으면, 
        end = mid - 1 # h 감소 
answer = end
print(end)