
# 1은 육지, 0은 물, 
# 섬의 개수를 구하라. (연결 되어 있는 1의 덩어리 개수)

# 네 방향 각각 dfs 재귀를 이용해 탐색을 끝마치면 1이 증가하는 형식으로 육지의 개수를 파악 가능 할 듯.

# test case 1
# 출력 : 1
# arr = [
#     [1, 1, 1, 1, 0],
#     [1, 1, 0, 1, 0],
#     [1, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0]
# ]

# test case 2
# 출력 : 3
#
arr = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1,]
]

def dfs(arr, i, k):
    # 범위를 벗어 나거나 육지가 아니면 종료
    if i < 0 or i >= len(arr) \
            or k < 0 or k >= len(arr[0]) \
                or arr[i][k] != 1:
        return

    arr[i][k] = 0 # 방문한 곳은 중복을 방지하기 위해 물로 갱신

    # 좌, 우, 상, 하 탐색
    dfs(arr, i + 1, k)
    dfs(arr, i - 1, k)
    dfs(arr, i, k + 1)
    dfs(arr, i, k - 1)


def main(arr):
    # 예외 처리
    if not arr:
        return 0

    count = 0
    for i in range(len(arr)):
        for k in range(len(arr[0])):
            if arr[i][k] == 1:
                dfs(arr, i, k) # 해당 위치에서 탐색할 수 있는 모든 육지를 탐색한 후, 카운트 1증가.
                count += 1
    return count

print(main(arr))

# nested function

