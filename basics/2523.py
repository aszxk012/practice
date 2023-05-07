# 2523
# 별 찍기

num = int(input())

for i in range(1, num + 1):
    print("*" * i)

for j in range(num, 1, -1):
    print("*" * (j - 1))