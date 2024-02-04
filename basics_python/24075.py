# 24075
# 두 수가 주어졌을 때 두 수를 더한 값, 두 수를 뺀 값을 출력한다.

a, b = map(int, input().split(' '))
sum = a + b
minus = a - b

if (sum >= minus):
    print(sum)
    print(minus)

else:
    print(minus)
    print(sum)