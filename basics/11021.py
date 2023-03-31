# 11021
# 테스트 케이스 개수를 받아 Case #x: a+b를 출력하기
# 테스트 케이스 번호는 1번부터 시작

num = int(input())
result = []

for i in range(num):
    char = input()
    x, y = char.split(' ')
    x, y = int(x), int(y)
    total = x + y

    result.append(total)


for i in range(len(result)):
    print("Case #" + str(i + 1) + ":", result[i])