def solution(strings, n):
    # 풀이 1
    # strings.sort() # 사전순으로 정렬
    # return sorted(strings, key = lambda x : x[n]) # 사전순으로 정렬된 데이터를 인덱스 n을 기준으로 정렬하여 return

    # 풀이 2
    return sorted(strings, key = lambda x : (x[n], x))

# 설명
# - sort, sorted() 메서드에 key 인자를 전달하여 기준을 정할 수 있음.
# → key를 기준으로 정렬을 하게되면 나머지 요소들은 영향을 끼치지 못하고 기존 순서를 유지한다.

#-----------------------------------------------------------------------

# 풀이
# 1. return을 하기전에 sort()를 하여 사전순으로 미리 정렬하기
# 2. 람다함수에 우선순위를 설정할 수 있다.