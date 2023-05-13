# 2739
# n을 입력받아 n단 구구단 출력하기

num = int(input())

for i in range(1, 10):
    result = num * i
    print(num, "*", i, "=", result)