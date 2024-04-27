# 31607
# 정수 A, B, C가 주어진다.
# 어느 한 값이 나머지 두 값의 합과 같다면 1, 그렇지 않다면 0 출력

a = int(input())
b = int(input())
c = int(input())

sum_a = a + b
sum_b = b + c
sum_c = a + c

if (c == sum_a):
    print(1)
elif (a == sum_b):
    print(1)
elif (b == sum_c):
    print(1)
else:
    print(0)