# 27433
# N! 출력하기

n = int(input())
result = 1

for i in range(1, n + 1):
    result *= i

print(result)