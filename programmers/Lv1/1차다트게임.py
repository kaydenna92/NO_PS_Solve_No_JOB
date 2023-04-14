    # S, D, T : 1제곱, 2제곱, 3제곱
    # 스타상(*) : 해당 점수와 바로 전에 얻은 점수를 2배로 만든다.
    # 스타상은 첫 번째 기회에서도 나올 수 있다. 이 경우, 첫 번재 스타상의 점수만 2배가 된다
    # 스타상의 효과는 다른 스타상의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상 점수는 4배가 된다

    # 아차상(#) : 해당 점수를 마이너스로 만든다.
    # 스타상과 아차상의 효과는 중첩될 수 있다. 이 경우 중첩된 아차상의 점수는 -2배가 된다


def solution(dartResult):
    answer = []
    temp = ''
    number = 0

    for dart in dartResult:
        try:
            temp += dart
            number = int(temp) # 숫자가 아닌 문자열이 있는 경우, 에러가 나므로 except로 이동
        except:
            temp = '' # temp 초기화

            if dart == "S":
                number **= 1
                answer.append(number)

            elif dart == "D":
                number **= 2
                answer.append(number)

            elif dart == "T":
                number **= 3
                answer.append(number)

            elif dart == "*":
                if len(answer) == 1: # 스타상이 첫 번째 기회에 나오는 경우,
                    answer[0] *= 2 # 첫 번째 점수만 2배로!

                if len(answer) >= 2: # 이후의 경우,
                    answer[-1] = answer[-1] * 2
                    answer[-2] = answer[-2] * 2
            elif dart == "#": # 아차상의 경우,
                answer[-1] = answer[-1] * (-1) # 해당 점수를 마이너스로 변환

    return sum(answer)

solution("1S2D*3T")
solution("1D2S#10S")
solution("1D2S0T")
solution("1S*2T*3S")
solution("1T2D3D#")
solution("1D2S3T*")
