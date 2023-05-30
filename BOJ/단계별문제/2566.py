# 최댓값이 몇 행, 몇 열에 위치한 수인지 구하는 프로그램

def find_max(array):
    max_value  = -99999999999999999999
    y, x = 0, 0
    for i in range(len(array)):
        for k in range(len(array[i])):
            if array[i][k] > max_value:
                max_value = array[i][k]
                y = i
                x = k
    return [max_value, y, x]

def main():
    board = [list(map(int, input().split())) for _ in range(9)]
    MAX, y, x = find_max(board)

    print(MAX)
    print(y + 1, x + 1)


        
main()