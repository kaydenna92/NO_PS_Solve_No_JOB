n=int(input()) 
s=[int(input()) for _ in range(n)] 

memo=[0]*(n) # 점수의 합 저장하는 리스트

if len(s)<=2: # 2개 이하의 경우, 
    print(sum(s))

else: # 3개 이상인 경우,
    memo[0]=s[0] # 1번째 계단
    memo[1]=s[0]+s[1] # 2번째 계단
    for i in range(2,n): # 3번째 계단부터, 조건에 맞게!
        memo[i]=max(memo[i-3]+s[i-1]+s[i], memo[i-2]+s[i])
    print(memo[-1])