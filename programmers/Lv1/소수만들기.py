import math
def is_prime_number(number): # 소수인지 아닌지 판별하는 function
    
    for i in range(2, int(math.sqrt(number)) + 1): # int(number ** 2) + 1, 에라토스테네스의 체
        
        if number % i == 0:
            return False
        
    return True

def solution(nums):
    answer = 0
    choices = []
    
    # 조합을 위한 DFS 
    def dfs(level, r, visited): 
        nonlocal nums
        
        if len(visited) == r: 
            choices.append(visited[:])
            return

        for i in range(level, len(nums)):
            dfs(i + 1, r, visited + [nums[i]])

    dfs(0, 3, [])

    # choices를 탐색, 각각의 element들의 합이 소수인지 판별
    for choice in choices:
        if is_prime_number(sum(choice)):
            answer += 1
        
    return answer
