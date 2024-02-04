# 13136
# 좌석의 세로 크기, 가로 크기, 한 대의 CCTV가 수용할 수 있는 범위(n행 n열까지)가 주어진다.
# 모든 좌석을 전부 촬영하도록 CCTV를 배치할 때, 최소 몇 개의 CCTV가 필요한지 출력

r, c, n = map(int, input().split(' '))

y = r // n
x = c // n

if (r % n != 0):
    y += 1
if (c % n != 0):
    x += 1

print(x * y)