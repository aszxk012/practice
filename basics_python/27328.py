# 27328
# 두 정수가 주어질 때 a < b면 -1, a = b면 0, a > b면 1 출력하기

a = int(input())
b = int(input())

if a < b:
    print(-1)
elif a == b:
    print(0)
else:
    print(1)