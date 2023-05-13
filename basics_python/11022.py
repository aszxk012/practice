# 11022
# 테스트 케이스 개수를 받아 Case #x: A + B = C 형식으로 출력하기
# 테스트 케이스 번호는 1번부터 시작

num = int(input())
result = []
front_num = []
back_num = []

for i in range(num):
    char = input()
    x, y = char.split(' ')
    x, y = int(x), int(y)

    front_num.append(x)
    back_num.append(y)

    total = x + y

    result.append(total)


for i in range(len(result)):
    print("Case #" + str(i + 1) + ":", front_num[i], "+", back_num[i], "=", result[i])