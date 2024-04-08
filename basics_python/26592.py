# 26592
# 넓이와 밑변의 길이가 주어진 삼각형의 높이 찾기

n = int(input())

for i in range(n):
    a, b = map(float, input().split(' '))
    h = 2 * a / b

    print("The height of the triangle is %.2f units" % h)