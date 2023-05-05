# 자동차 생산하는 a, b 조립라인이 존재
# 두 조립라인에는 n개의 작업장이 존재
# 동일작업 수행, 작업시간은 다름
# 다른 조립라인으로 제품이동이 가능
# 자동차 1대의 가장 빠른 조립 시간을 구하기



N = int(input())
assemblyLine = []
moveLine = []
for i in range(N - 1):
    a, b, atob, btoa = map(int, input().split())
    assemblyLine.append([a, b])
    moveLine.append([atob, btoa])
assemblyLine.append(list(map(int, input().split())))



# 초기화 # 공정마다 생산비용을 넣기 위해 * N
A_Line = [assemblyLine[0][0]] * N
B_Line = [assemblyLine[0][1]] * N

for i in range(1, N):
    a, b = assemblyLine[i]
    atob, btoa = moveLine[i - 1]

    # A라인에서만 생산한 시간 vs B라인으로 이동한 후 생산시간 비교
    A_Line[i] = min(A_Line[i - 1] + a, B_Line[i - 1] + btoa + a)
    
    # B라인에서만 생산한 시간 vs A라인으로 이동한 후 생산시간 비교
    B_Line[i] = min(B_Line[i - 1] + b, A_Line[i - 1] + atob + b)

print(min(A_Line[N - 1], B_Line[N - 1]))