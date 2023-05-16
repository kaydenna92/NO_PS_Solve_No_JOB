while True:
    n = int(input())
    if n == -1:
        break
    yaksu = []
    for i in range(1, n):
        if n % i == 0:
            yaksu.append(i)

    yaksu.sort()
    if sum(yaksu) == n:
        print('{0} ='.format(n), end=' ')
        for i in range(0, len(yaksu) - 1):
            print('{0} +'.format(yaksu[i]), end=' ')
        print(yaksu[-1])
    else:
        print('{} is NOT perfect.'.format(n), end=' ')