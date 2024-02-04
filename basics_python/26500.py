# 26500
# 수직선 상의 두 점 사이의 거리 출력하기
# 소수점 두 번쩨 자리에서 반올림하여 소수점 한 자리까지 출력

n = int(input())

for i in range(n):
    a, b = map(float, input().split(' '))
    abs_a, abs_b = abs(a), abs(b)
    dis = 0
        
    if (a < b):
        dis = b - a
    else:
        dis = a - b

    if (dis < 0):
        dis = abs_a + abs_b

    print("%.1f" % (dis))