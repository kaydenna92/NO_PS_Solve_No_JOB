def R(number):
    from collections import deque

    number = str(number)
    temp = deque([0] * 4)

    for i in range(len(number)): # 1234 / 123
        if len(number) > 3:
            temp[i] = number[i]
        elif len(number) > 2: # 123
            temp[i+1] = number[i]
        elif len(number) > 1: # 12
            temp[i + 2] = number[i]
        else: # 1
            temp[i + 3] = number[i]
                
    right = temp.pop()
    temp.appendleft(right)

    return int(''.join(map(str, temp)))

print(R((1234)))
print(R((123)))
print(R((12)))
print(R((1)))

