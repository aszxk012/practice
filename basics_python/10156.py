# 10156
# 과자 한 개의 가격, 과자의 개수, 가진 돈을 입력받아 추가 금액 계산하기

char = input()
num, price, money = char.split(' ')
num, price, money = int(num), int(price), int(money)
add_money = 0

if (num * price) > money:
    add_money = (num * price) - money

else:
    pass

print(add_money)