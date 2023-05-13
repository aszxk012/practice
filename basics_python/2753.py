# 2753
# 윤년 판별하는 프로그램
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐때, 또는 400의 배수일때

year = int(input())

if (year % 4 == 0) & (year % 100 != 0):
    print("1")
    
elif (year % 4 == 0) & (year % 400 == 0):
    print("1")

else:
    print("0")