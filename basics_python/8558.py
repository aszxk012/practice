# 8558
# n!의 일의 자리 수 출력

n = int(input())

if (n < 5):
    if ((n == 0) or (n == 1)):
        print(1)
    elif (n == 2):
        print(2)
    elif (n == 3):
        print(6)
    elif (n == 4):
        print(4)
else:
    print(0)