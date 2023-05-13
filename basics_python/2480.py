# 2480
# 주사위 게임으로 얻을 수 있는 상금 계산하는 프로그램

# 같은 눈 3개 > 10,000 + (같은 눈) * (1,000)
# 같은 눈 2개 > 1,000 + (같은 눈) * 100
# 모두 다른 눈 > (가장 큰 눈) * 100

dice = input()
x, y, z = dice.split(' ')
x, y, z = int(x), int(y), int(z)

if (x == y) & (y == z):
    print(10000 + x * 1000)

elif (x == y):
    print(1000 + x * 100)
elif (y == z):
    print(1000 + y * 100)
elif (x == z):
    print(1000 + x * 100)

else:
    if (x > y):
        if (x > z):
            print(x * 100)

        elif (x < z):
            print(z * 100)
    
    elif (x < y):
        if (z < y):
            print(y * 100)
        
        elif(z > y):
            print(z * 100)