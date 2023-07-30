# 5585
# 1000엔 냈을 때 잔돈의 개수 구하기

price = int(input())
count = 0
change = 1000 - price

rest_list = [500, 100, 50, 10, 5, 1]

for rest in rest_list:
    while True:
        if change >= rest:
            change -= rest
            count += 1

        else:
            break

print(count)