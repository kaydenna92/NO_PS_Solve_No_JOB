data = [list(input()) for _ in range(5)]
answer = ''

max_length = len(data[0])
for d in data:
    if len(d) > max_length:
        max_length = len(d)


for i in range(max_length):
    for k in range(5):
        if i < len(data[k]):
            answer += data[k][i]

print(answer)
ssdsjqwsqwqwqwqwqwqw