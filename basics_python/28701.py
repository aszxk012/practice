# 28701
# 1 ~ N까지의 수의 합, 그 수를 제곱한 수와 1 ~ N까지의 수의 세제곱 합 구하기

num = int(input())

sum = 0
sq = 1
sq_3 = 1

for i in range(num):
    sum += i + 1
    sq_3 += (i + 1) ** 3

sq = sum ** 2

print(sum)
print(sq)
print(sq_3 - 1)