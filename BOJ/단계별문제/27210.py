# 깨달음의 양 = 왼쪽(1) - 오른쪽(2)

# 구간의 합의 최대를 구해서 색 칠하기~
n = int(input())
enlightenments = list(map(int, input().split()))
count_left = [0] * n
count_right = [0] * n

count_left[0] = 1 if enlightenments[0] == 1 else 0
count_right[0] = 1 if enlightenments[0] == 2 else 0

for i in range(1, n):
    if enlightenments[i] == 1:
        count_left[i] = count_left[i - 1] + 1

    else:
        if count_left[i - 1] > 0:
            count_left[i] = count_left[i - 1] - 1
        else:
            count_left[i] = 0

for i in range(1, n):
    if enlightenments[i] == 2:
        count_right[i] = count_right[i - 1] + 1

    else:
        if count_right[i - 1] > 0:
            count_right[i] = count_right[i - 1] - 1
        else:
            count_right[i] = 0

print(max(max(count_left), max(count_right)))
