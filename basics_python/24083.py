# 24083
# 시침이 가리키는 눈금을 a, 이 상태로부터 b시간이 지난 후의 눈금(숫자) 출력하기

a = int(input())
b = int(input())
si = a + b

while True:
    if (si <= 12):
        print(si)
        break
    else:
        si -= 12