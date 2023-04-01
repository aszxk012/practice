# 10951
# 여러 개의 테스트 케이스 입력받아 A+B 출력하기
# EOF

result = []

while True:
    try:
        char = input()
        x, y = char.split(' ')
        x, y = int(x), int(y)

        result.append(x + y)

    except EOFError:
        break

for i in range(len(result)):
    print(result[i])