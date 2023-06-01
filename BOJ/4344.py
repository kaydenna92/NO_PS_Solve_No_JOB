c = int(input())
student_score = [list(map(int, input().split())) for _ in range(c)]

for i in range(c):
    student = student_score[i][0]
    average = sum(student_score[i][1:]) / student
    count = 0
    # print(average)
    for k in range(student_score[i][0]):
        if student_score[i][k+1] > average:
            count += 1
    
    percent = (count / student_score[i][0]) * 100
    print('%.3f' %percent + '%')