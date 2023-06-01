

def count(target, array):
    cnt = 0
    for number in array:
        if number == target:
            cnt += 1

    return cnt


def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    v = int(input())

    print(count(v, numbers))

main()