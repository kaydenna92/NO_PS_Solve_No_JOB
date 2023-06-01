work = dict()
for i in range(30):
    work[i+1] = False

for _ in range(28):
    done = int(input())
    work[done] = True

for k, v in work.items():
    if not v:
        print(k)