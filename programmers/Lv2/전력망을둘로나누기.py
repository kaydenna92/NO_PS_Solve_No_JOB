from collections import Counter

def findboss(a):
    global arr
    if arr[a-1] == a:
        return a
    return findboss(arr[a-1])


def union(a, b):
    global arr
    a_boss, b_boss = findboss(a), findboss(b)
    if a_boss == b_boss:
        return
    if a_boss < b_boss:
        arr[b-1] = a_boss
    else :
        arr[a-1] = b_boss


def solution(n, wires):
    global arr
    answer = n
    for w in range(len(wires)):
        if wires[w][0] > wires[w][1]:
            wires[w] = [wires[w][1],wires[w][0]]
    wires.sort()
    print(wires)
    for i in range(len(wires)):
        arr = [i+1 for i in range(n)]
        for j in range(len(wires)):
            if i == j: continue
            union(wires[j][0], wires[j][1])

        count = sorted(Counter(arr).items())
        print(count)
        answer = min(answer, abs(count[0][1]-count[1][1]))

    return answer


print(solution(8, [[1,2],[1,3],[1,4],[4,5],[5,6],[6,7],[6,8]]))
