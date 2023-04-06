# def solution(n, lost, reserve):
#     persons = [True for i in range(n)]

#     for i in lost:
#         persons[i - 1] -= 1

#     for i in reserve:
#         persons[i - 1] += 1

#     for i, v in enumerate(persons):
#         print(i, v)
#         if i > 0 and v == 0 and persons[i - 1] == 2: # 맨 앞의 학생은 뒤 학생에게만 빌릴 수 있음 -> i > 0, 체육복이 없을때, 그리고 앞의 학생이 여벌있을때,
#             persons[i] = 1 
#             persons[i - 1] = 1
#         elif i < n - 1 and v == 0 and persons[i + 1] == 2: # 맨 뒤의 학생은 앞의 학생에게만 빌릴 수 있음 / 뒤 학생이 여벌이 있을 때, 
#             persons[i] = 1
#             persons[i + 1] = 1

#     return n - persons.count(0)

# solution(5, [2, 4], [1, 3, 5])


def solution2(n, lost, reserve):
    answer = 0
    cloths = [1 for i in range(n)]
    dont_have_cloth = list(set(lost) - set(reserve))

    for i in reserve:
        cloths[i - 1] += 1
    
    for i in dont_have_cloth:
        cloths[i - 1] -= 1
    

    for i in range(len(cloths)):
        if i > 0 and cloths[i] == 0 and cloths[i - 1] == 2:
            cloths[i] = 1
            cloths[i - 1] = 1
        elif i < n - 1 and cloths[i] == 0 and cloths[i + 1] == 2:
            cloths[i] = 1
            cloths[i + 1] = 1

    print(cloths)
    

    return n - cloths.count(0)

print(solution2(5, [2,4], [1,3,5]))