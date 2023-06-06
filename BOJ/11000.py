# 현재 강의가 끝나는 시간보다 다음 강의 시작시간이 빠르면 강의실 하나가 더 필요함
# 현재 강의가 끝나는 시간보다 다음 강의 시작시간이 느리면 해당 강의실에서 계속 할 수 잇음.
import heapq, sys


input = sys.stdin.readline
n = int(input())
lecture = [list(map(int, input().split())) for _ in range(n)]
lecture.sort() # 시작시간을 기준으로 정렬.

lecture_Q = []
heapq.heappush(lecture_Q, lecture[0][1]) # 첫 번째 강의 종료 시간을 PQ에 추가

for i in range(1, n): # 2번째 강의부터 ~ 마지막 강의까지 탐색(두 번째 강의부터 첫 강의와 비교)
    if lecture[i][0] < lecture_Q[0]: # 다음 강의의 시작시간이 이전 강의의 종료 시간보다 빠르면,
        heapq.heappush(lecture_Q, lecture[i][1]) # 해당 강의의 종료 시간을 PQ에 추가(강의실 생성)

    else: # 느리면 강의실 생성 필요 X
        heapq.heappop(lecture_Q) # 이전 강의의 종료시간 제거
        heapq.heappush(lecture_Q, lecture[i][1]) # 해당 강의의 종료시간을 PQ에 추가!


print(len(lecture_Q)) # PQ의 길이가 최소 강의실 개수.


