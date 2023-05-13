# 2522
# 오른쪽 정렬하여 별찍기

num = int(input())

for i in range(1, num + 1):
    print(" " * (num - i) + "*" * i)

for j in range(num, 1, -1):
    print(" " * (num - j + 1) + "*" * (j - 1))