# from collections import defaultdict
# def solution(N, stages):
#     answer = []
#     for_calculate_dict = defaultdict(int)
#
#     def fail(stage):
#         nonlocal stages
#
#         present_stage_player = 0
#         passed_player = 0
#
#         for i in range(len(stages)):
#
#             if stages[i] == stage:
#                 present_stage_player += 1
#
#             if stages[i] > stage:
#                 passed_player += 1
#
#         return [stage, present_stage_player, passed_player]
#
#     temp = [0] * (N)
#     for stage in range(1, N + 1):
#         stage, present, passed = fail(stage)
#
#         if present == 0:
#             temp[stage - 1] = [stage, 0]
#
#         elif passed == 0:
#             temp[stage - 1] = [stage, 100]
#
#         else:
#             temp[stage - 1] = [stage, ((present) / (present + passed)) * 100]
#
#     print(temp)
#     # for idx, value in for_calculate_dict.items():
#     #     temp[idx - 1] = [idx, value]
#
#     temp.sort(key = lambda x: (x[1], -x[0]), reverse = True)
#     answer = [i[0] for i in temp]
#     return answer
#
#
# print(solution(5, [2,1,2,6,2,4,3,3]))


def solution(N, stages):
    answer = []
    fail = []
    info = [0] * (N + 2)

    for stage in stages:
        info[stage] += 1

    for i in range(N):

        be = sum(info[(i + 1):]) # stage가 1일때, -> sum(스테이지 클리어 플레이어 + 통과하지 못한 플레이어)p
        yet = info[i + 1] # 아직 머물러 있는 플레이어 #

        if be == 0: # 모두 클리어한 경우, 실패율은 0,
            fail.append((str(i + 1), 0))

        else: # 클리어 못한 경우가 있을 때,
            fail.append((str(i + 1), yet / be))

    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(int(item[0]))

    return answer

print(solution(5, [2,1,2,6,2,4,3,3]))