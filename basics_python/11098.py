# 11098
# 가장 비싼 선수 출력하기

import sys

test = int(input())

for i in range(test):
    p = int(input()) # 고려해야할 선수의 수
    max_price = -sys.maxsize - 1
    max_name = ''
    
    for j in range(p):
        price, name = input().split(' ')
        price = int(price)

        max_price = max(max_price, price)
        
        if (max_price == price):
            max_name = name
        
    print(max_name)
    
    