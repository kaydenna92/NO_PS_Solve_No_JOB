# cards1, cards2 의 인덱스를 저장해놓고,
# goals에 있는 각각의 요소들의 인덱스를 비교한다
# 예를 들어 cards1에 있는 요소들의 인덱스를 탐색해서 저장하고,
# goals에 있는 cards1의 요소들의 인덱스를 탐색하고, 만약에 어떠한 요소가 다른 요소보다 뒤에 나와야하는데 앞에 나와있다면 No, 아니라면 yes


def solution(cards1, cards2, goal):
    answer = "YES"

    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)

        elif len(cards2) > 0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "NO"

    # if len(goal) > 0:
    #     print(False)
    # else:
    #     print(True)
    return answer

cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

# print(solution(cards1, cards2, goal))
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))