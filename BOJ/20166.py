n, m, k = map(int, input().split())
dy = [0, 1, 0, -1, -1, 1, 1, -1]
dx = [1, 0, -1, 0, 1, 1, -1, -1]

words = []
god_words = {} 
god_words_list = []

for _ in range(n):
    words.append(list(input()))

for _ in range(k):
    char = input()
    god_words[char] = 0
    god_words_list.append(char)


def func(x, y, cnt, string):
    if cnt > 5: # 신이 좋아하는 문자열의 길이는 5 이하 
        return
    
    # n * m 2차원 리스트를 탐색하여 만약 문자가 god_words에 있다면, + 1
    if string in god_words:
        god_words[string] += 1 # 경우의 수 저장

    # 8 방향 탐색
    for i in range(8):
        nx, ny = (x + n + dx[i]) % n, (y + m + dy[i]) % m # 범위 제한
        func(nx, ny, cnt + 1, string + words[nx][ny])


# n * m 2차원 리스트를 탐색
for i in range(n):
    for k in range(m):
        start = ''
        func(i, k, 1, start + words[i][k]) 


# 위의 과정이 끝난 후에 go
for word in god_words_list:
    if word in god_words:
        print(god_words[word]) # 딕셔너리의 해당값을 출력