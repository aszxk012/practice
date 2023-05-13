# 7891
# 테스트 케이스 입력 받아 두 수 더하기

test = int(input())
result = []
for _ in range(test):
    a, b = input().split()
    a, b = int(a), int(b)

    result.append(a + b)

for i in range(test):
    print(result[i])