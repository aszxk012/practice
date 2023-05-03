# 5565
# 첫번째 줄에는 책 10권의 총 가격을, 두번째 줄부터는 책 9권 각각의 가격을 입력한다
# 가격을 알 수 없는 한 권의 가격을 구해 출력하기

total_price = int(input())
cur_price = 0

for _ in range(9):
    price = int(input())
    cur_price += price

print(total_price - cur_price)