# 9713
# 테스트 개수 입력받아 연속으로 더하기

test = int(input())
sum = 0
result = []

for _ in range(test):
    num = int(input())

    for i in range(num // 2 + 1):
        sum += 2 * i + 1

    result.append(sum)
    sum = 0

for i in range(test):
    print(result[i])