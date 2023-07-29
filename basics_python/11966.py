# 11966
# 자연수 n이 2의 제곱이면 1, 아니면 0 출력하기
# log 말고 비트 연산으로 다시 풀어보기(2023.07.26)
import math

n = int(input())

if n != 1:
    if (n % 2 != 0):
        print(0)
    else:
        a = math.log(n, 2)
        if not a - int(a):
            print(1)
        else:
            print(0)

else:
    print(1)

# 비트 연산 이용하여 풀기(2023.07.29)

n = int(input())

if n > 0 and (n & (n - 1)) == 0:
    print(1)
else:
    print(0)