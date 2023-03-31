# 10952
# 여러 개의 케이스 A + B 출력하기
# 입력의 마지막에 0 두개가 들어온다.

front_num = []
back_num = []

while True:
    char = input()
    x, y = char.split(' ')
    x, y = int(x), int(y)
    
    if char == '0 0':
        break

    else:
        front_num.append(x)
        back_num.append(y)

for i in range(len(front_num)):
    print(front_num[i] + back_num[i])