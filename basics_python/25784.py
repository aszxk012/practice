# 25784
# 세 개의 중복이 없는 0이 아닌 정수가 주어질 때
# 세 개 중 두 개의 정수를 사용하여 하나를 계산하는 방법을 결정해야한다.
# 세 숫자 중 하나가 다른 숫자의 합이면 1을, 곱이면 2를, 그렇지 않으면 3을 출력

a, b, c = map(int, input().split(' '))
num_list = [a, b, c]
max_num = max(num_list)

if (max_num == a):
    if (a == b + c):
        print(1)
    elif (a == b * c):
        print(2)
    else:
        print(3)

elif (max_num == b):
    if (b == a + c):
        print(1)
    elif (b == a * c):
        print(2)
    else:
        print(3)

elif (max_num == c):
    if (c == a + b):
        print(1)
    elif (c == a * b):
        print(2)
    else:
        print(3)