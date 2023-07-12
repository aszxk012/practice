test = int(input())

for i in range(test):
    sum = 0
    
    car_price = int(input())
    option_num = int(input())
    
    for j in range(option_num):
        op_cnt, op_price = map(int, input().split(' '))
        sum += op_cnt * op_price
    sum += car_price
    print(sum)