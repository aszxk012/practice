num = int(input())

for i in range(num):
    for j in range(num):
        if (i % 2 == 0):
            print("* ", end = '')
        else:
            print(" *", end = '')
    print()