# 22193
# 숫자의 자릿수가 입력되고 a, b가 하나씩 주어진다.
# a, b 곱하기

n, m = map(int, input().split(' '))
a = input()
b = input()

if len(a) == n and len(b) == m:
    a = int(a)
    b = int(b)
    
    print(a * b)