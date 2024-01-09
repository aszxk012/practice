# 22155
# 조건문의 수와 반복문의 수가 주어질 때 해당 문제가 간단한 문제인지 판단
# 간단한 문제의 기준은 조건문 하나, 반복분 두개 또는 조건문 두개, 반복문 하나를 넘지 않는 문제이다.

n = int(input())

for i in range(n):
    condition, loop = map(int,input().split(' '))

    if ((condition < 2) and (loop < 3)):
        print("Yes")
    elif ((condition < 3) and (loop < 2)):
        print("Yes")
    else:
        print("No")