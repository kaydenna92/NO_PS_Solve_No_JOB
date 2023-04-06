# # 출연한 가수의 점수가 지금까지 출연 가수들의 점수 중 상위 k번째 이내이면 해당 가수의 점수를 명예의 전당에 올린다.
# # 즉, 프로그램 시작 이후 초기에 k일까지는 모든 출연 가수의 점수가 명예의 전당에 오른다.
# # k일 이후에는 위의 조건에 따라 전당에 올리고, 기존의 마지막 k번째의 순위는 내려가게 된다.

# # 매일 발표된 명예의 전당의 최하위 점수를 return


# def solution(k, score):
#     rank_board = []
#     report = []

#     for i in range(1, len(score) + 1):
#         rank_board.append(score[i - 1])

#         if len(rank_board) > k: # k일 이후,

#             rank_board.sort(reverse=True)
#             del rank_board[-1]
#             report.append(rank_board[-1])

#         else: # 초기에 k일까지,

#             rank_board.sort(reverse=True)
#             report.append(rank_board[-1])

#     return report

# solution(3, [10, 100, 20, 150, 1, 100, 200])


def solution(k, score):
    rank_board = []
    answer = []

    for s in score:
        rank_board.append(s)

        if len(rank_board) > k:
            rank_board.remove(min(rank_board))
            
        answer.append(min(rank_board))

    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))