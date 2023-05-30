# 전공평점이 3.3 이상이거나 졸업고사를 통과해야 졸업된다.
# 전공평점을 계산하는 프로그램을 작성

# 전공평점 = 전공과목별 (학점 * 과목 평점)의 합을 학점의 총합으로 나눈 값

grade_and_score = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0.0
}

total = 0
total_credit = 0
for _ in range(20):
    subject, credit, grade = input().split()
    if grade == 'P':
        continue
    else:
        total += grade_and_score[grade] * float(credit)
        total_credit += float(credit)

    
print(round(total / total_credit, 6))
