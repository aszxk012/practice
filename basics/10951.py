# 10951
# 여러 개의 테스트 케이스 입력받아 A+B 출력하기

front_num = []
back_num = []

while True:
    try:
        char = input()
        x, y = char.split(' ')
        x, y = int(x), int(y)

        front_num.append(x)
        back_num.append(y)

    except EOFError:
        break

for i in range(len(front_num)):
    print(front_num[i] + back_num[i])