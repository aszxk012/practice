# 24087
# 기본으로 제공되는 아이스크림은 250엔에 Acm, 추가로 제공되는 아이스크림은 200엔에 Bcm이다.
# 높이가 Scm 이상인 아이스크림을 구매하고 싶을 때 필요한 최소 금액 출력

s = int(input())
a = int(input())
b = int(input())
current = 0
i, price = 0, 0

while (current < s):
    if (i == 0):
        current += a
        price += 250
    else:
        current += b
        price += 100
    i += 1

print(price)