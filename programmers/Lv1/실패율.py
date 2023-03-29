from collections import defaultdict
def solution(N, stages):
    answer = []
    for_calculate_dict = defaultdict(int)

    def fail(stage):
        nonlocal stages

        present_stage_player = 0
        passed_player = 0

        for i in range(len(stages)):

            if stages[i] == stage:
                present_stage_player += 1

            if stages[i] > stage:
                passed_player += 1

        return [stage, present_stage_player, passed_player]
    
    temp = [0] * (N)
    for stage in range(1, N + 1):
        stage, present, passed = fail(stage)

        if present == 0:
            temp[stage - 1] = [stage, 0]

        elif passed == 0:
            temp[stage - 1] = [stage, 100]

        else:
            temp[stage - 1] = [stage, ((present) / (present + passed)) * 100]

    print(temp)
    # for idx, value in for_calculate_dict.items():
    #     temp[idx - 1] = [idx, value]
    
    temp.sort(key = lambda x: (x[1], -x[0]), reverse = True)
    answer = [i[0] for i in temp]
    return answer


print(solution(5, [2,1,2,6,2,4,3,3]))