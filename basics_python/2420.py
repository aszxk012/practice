# 2420
# 두 수의 차이 구하기

a, b = map(int, input().split(' '))

if a > b:
    b = -b
else:
    a = -a

print(a + b)