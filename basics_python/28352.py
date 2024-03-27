# 28352
# 10!초는 6주와 같다.
# N!초는 몇 주인지 출력

n = int(input())

fac = 3628800
week = 1

if (n == 10):
    week = 6
    print(week)

else:
    for i in range(11, n + 1):
        fac *= i

    week = int(fac / 3600 / 24 / 7)

    print(week)