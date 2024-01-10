# 24079
# A지점에서 B지점으로 이동하는데 X시간, B지점에서 C지점으로 이동하는데 Y시간 걸릴 때
# A지점에서 B지점을 경유해 C지점으로 이동할 때, Z시간 30분 이내에 이동 가능한지 판단
# 이동 가능하다면 1, 불가능하다면 0 출력

x = int(input())
y = int(input())
z = int(input()) + 0.5

sum = x + y

if (sum > z):
    print(0)
else:
    print(1)