def input_data():
    number = []
    while True:
        a, b = map(int, input().split())

        if a == 0 and b == 0:
            break
        else:
            number.append([a, b])
    return number


def calc(data):
    for i in range(len(data)):
        a, b = data[i][0], data[i][1]
        if a < b:
            if b % a == 0:
                print('factor')
            if b % a != 0:
                print('neither')
        else:
            if a % b == 0:
                print('multiple')
            else:
                print('neither')

data = input_data()
calc(data)