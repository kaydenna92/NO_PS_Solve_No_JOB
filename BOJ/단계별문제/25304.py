# 영수증
# 구매한 각 물건의 가곆과 개수
# 구매한 물건들의 총 금액을 보고 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사
def calculator(price, count):
    cal_price = price * count
    return cal_price


receipt_price = int(input())
n = int(input())

total_price = 0
for _ in range(n):
    a, b = map(int, input().split())
    total_price += calculator(a, b)

if receipt_price == total_price:
    print('Yes')
else:
    print('No')


