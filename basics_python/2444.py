# 2444
# 다이아몬드 형태로 별 찍기

num = int(input())

for i in range(1, num + 1):
    print(" " * (num - i) + "*" * ((2 * i) - 1))

for i in range(1, num):
    print(" " * (i) + "*" * ((num - i) * 2 - 1))