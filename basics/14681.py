# 14681
# 주어진 점이 어느 사분면에 속하는지 판별하는 프로그램

x = int(input())
y = int(input())

if (x > 0) & (y > 0):
    print('1')
elif (x > 0) & (y < 0):
    print('4')
elif(x < 0) & (y > 0):
    print('2')
elif(x < 0) & (y < 0):
    print('3')