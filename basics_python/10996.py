# 10996
# 별 찍기

num = int(input())

for i in range(2 * num):
    for j in range(num):
        if i % 2 == 0:
            if j % 2 == 0:
                print("*", end='')
            else:
                print(" ", end='')
        else:
            if j % 2 == 0:
                print(" ", end='')
            else:
                print("*", end='')

    print()