# n개의 지점 사이에 m개의 도로와 w개의 웜홀이 있음
# 도로는 방향이 없고, 웜홀은 방향이 존재
# 웜홀 : 시작 -> 도착을 하게 되면, 시작 했을때보다 시간이 뒤로 가게된다 / 시간이 거꾸로 간다.
# 한 지점에서 출발하여 다시 출발 했던 위치로 돌아왔을 때, 출발한 시각보다 시간이 ej 되돌아가 있는지 return

# 다익스트라??????
# 플로이드 워셜 : 시간초과......
# ?????????/
tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []
    distance = [999999999999] * (n + 1)

    for i in range(m + w):
        s, e, t = map(int, input().split())
        if i >= m:
            t = -t
        else:
            edges.append((e, s, t))
        edges.append((s, e, t))

    