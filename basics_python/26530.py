# 26530
# 제품 이름과 수량, 각 항목의 단가가 주어질 때
# 각 케이스별로 모든 상품의 총 금액을 소수점 두 자리로 반올림하여 출력

num = int(input())

for i in range(num):
    n = int(input())
    sum = 0

    for j in range(n):
        product, quantity, price = input().split(' ')
        quantity = int(quantity)
        price = float(price)

        sum += quantity * price
    
    sum = round(sum, 2)
    
    print("$%.2f" % (sum))