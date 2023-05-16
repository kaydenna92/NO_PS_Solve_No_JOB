# 숫자 1을 돌리는데 2초 소요
# 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
# 상근이의 할머니는 전화번호를 각 숫자에 해당하는 문자로 외운다.
# 각 알파벳에 해당하는 숫자를 걸면 된다
# UNUCIC  = 868242

phoneNumber = { 
    # 0: ['', 11],
    1: ['', 2],
    2: ['ABC', 3],
    3: ['DEF', 4],
    4: ['GHI', 5],
    5: ['JKL', 6],
    6: ['MNO', 7],
    7: ['PQRS', 8],
    8: ['TUV', 9],
    9: ['WXYZ', 10]
}

number = list(input())
answer = 0

for key, value in phoneNumber.items():
    for i in range(len(number)):
        if number[i] in value[0]:
            answer += value[1]
print(answer)