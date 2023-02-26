# 주어진 문자열이 팰린드롬인지 확인하라. 
# 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

# 입력
# A man, a plan, a canal: Panama
# 출력
# true

# 입력
# race a car
# 출력
# false

def solution(s):
    alphabet = []
    for alpha in s:
        if alpha.isalnum():
            alphabet.append(alpha.lower())

    while len(alphabet) > 1:
        if alphabet.pop(0) != alphabet.pop(): # list의 pop()함수는 인덱스를 지정할 수 있음.
            return False

    return True