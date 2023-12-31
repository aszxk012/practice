# 18411
# A, B, C가 주어질 때, 세 정수 중에서 높은 두 개를 더한 합계 출력하기

a, b, c = map(int, input().split(' '))

if (b <= c):
    max_int = max(a, b)
    print(max_int + c)

elif (a <= b):
    max_int = max(a, c)
    print(max_int + b)

elif (c <= a):
    max_int = max(b, c)
    print(max_int + a)

elif (c < b):
    max_int = max(a, c)
    print(max_int + b)

elif (b < a):
    max_int = max(b, c)
    print(max_int + a)

elif (a < c):
    max_int = max(a, b)
    print(max_int + c)