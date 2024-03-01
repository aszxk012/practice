# 8723
# 세 막대기의 길이가 주어진다.
# 세 막대기로 직각삼각형이나 정삼각형을 만들 수 없다면 0
# 직각삼각형만 만들 수 있다면 1,
# 정삼각형만 만들 수 있다면 2 출력

a, b, c = map(int, input().split(' '))
num_list = [a, b, c]
max_num = max(num_list)

if ((a == b) and (b == c)):
    print(2)

elif (max_num == a):
    cur = (b ** 2) + (c ** 2)
    
    if ((a ** 2) == cur):
        print(1)
    else:
        print(0)

elif (max_num == b):
    cur = (a ** 2) + (c ** 2)
    
    if ((b ** 2) == cur):
        print(1)
    else:
        print(0)

elif (max_num == c):
    cur = (a ** 2) + (b ** 2)
    
    if ((c ** 2) == cur):
        print(1)
    else:
        print(0)

else:
    print(0)