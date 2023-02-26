def solution(a, b, n):
    answer = 0
    
    while True:
        if n < a: 
            break
        n = n // 2
        answer += n
        
    
    return answer