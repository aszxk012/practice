# 5543
# 버거 3종류, 음료 2종류의 가격이 주어진다.
# 세트의 가격은 가격 합계에서 50원을 뺀 가격이다.
# 가장 싼 세트 메뉴의 가격 출력하기

burgers = []
drinks = []

for i in range(3):
    temp_bur = int(input())
    burgers.append(temp_bur)

for i in range(2):
    temp_dri = int(input())
    drinks.append(temp_dri)

min_bur = min(burgers)
min_dri = min(drinks)

print(min_bur + min_dri - 50)