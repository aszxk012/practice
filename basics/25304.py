# 25304
# 영수증 총 금액과 구매한 물건의 종류 수, 물건의 가격과 개수를 받아 금액 확인하기

total = int(input())
kinds = int(input())
prices = []
counts = []
total_price = 0

for i in range(kinds):
    kind = input()

    price, count = kind.split(' ')
    price, count = int(price), int(count)

    prices.append(price)
    counts.append(count)

for i in range(len(prices)):
    total_price += prices[i] * counts[i]

if total_price == total:
    print("Yes")
else:
    print("No")