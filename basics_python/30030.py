# 30030
# 부가가치세 10%를 포함한 가격 b가 주어질 때, 부가가치세를 제외한 가격 구하기

price_b = int(input())
price_a = price_b - (price_b // 11)
print(price_a)