# 10953
# A + B 출력하기

test = int(input())
result = []

for _ in range(test):
    a, b = map(int, input().split(','))
    result.append(a + b)

for i in range(len(result)):
    print(result[i])