# LCS : 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제.
# https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Sub%E3%85%81string%EC%99%80-Longest-Common-Subsequence#longest-common-subsequence-substring
# 부분수열에서 순서가 지켜지기 때문에 각 문자열들의 문자를 서로 비교하고 같으면 값을 1 증가시켜 누적값 구하기
#  acaypk, capcak

#   a c a y k p
# c 0 1 1 1 1 1
# a 1 1 2 2 2 2
# p 1 1 2 2 2 3
# c 1 2 2 2 2 3 
# a 1 2 3 3 3 3
# k 1 2 3 3 4 4

# (0, 1) : {c}, {a, c} 의 lcs 길이
# (1, 2) : {c, a}, { a, c, a}의 lcs 길이
# x번째 원소와 y번째 원소가 같으면 (x-1, y-1)의 lcs 길이의  + 1
word_1, word_2 = list(input()), list(input())
memo = [0] * len(word_2)

for i in range(len(word_1)):
    count = 0
    for j in range(len(word_2)):
        if count < memo[j]: # 글자가 다른 경우, 누적 값이 해당 위치의 값보다 작은 경우, 누적 값을 변경
            count = memo[j]
            
        elif word_1[i] == word_2[j]: # 같은 글자일 경우, 누적 값에서 1을 더한 값을 넣어주기
            memo[j] = count + 1

print(max(memo)) # 누적 값에는 이전 위치까지의 최대값이 계속해서 저장.


