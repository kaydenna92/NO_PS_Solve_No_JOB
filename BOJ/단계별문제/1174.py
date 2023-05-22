def make_descending(n):
    decrease = [0,1,2,3,4,5,6,7,8,9] 
    execution_count = 0
    desc_number = 0

    while decrease:
        pop_number = decrease.pop(0)
        execution_count += 1
        desc_number = pop_number

        if execution_count == n: 
            break

        for i in range(0, pop_number % 10):
            decrease.append(10 * pop_number + i)

    if execution_count < n:
        print(-1)
        
    else:
        print(desc_number)

n = int(input())
make_descending(n)
