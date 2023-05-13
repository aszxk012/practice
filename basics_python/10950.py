# 10950
# 테스트 개수를 입력받아 a+b 계산하기

num = int(input())
result = []

for i in range(num):
    char = input()
    x, y = char.split(' ')
    x, y = int(x), int(y)

    cur = x + y
    result.append(cur)

for i in range(len(result)):
    print(result[i])