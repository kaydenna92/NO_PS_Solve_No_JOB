import re


def isPalindrome1(s: str) -> bool:
    s = s.lower()
    s = re.sub('[a-z0-9]', '', s) # 정규식으로 불필요한 문자 필터링
    return s == s[::-1] # 슬라이싱


def isPalindrome2(s: str) -> bool:
    from collections import deque
    strs = deque()
    for char in s:
        if char.isalnum(): # 영문자와 숫자만 필터 통과
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


