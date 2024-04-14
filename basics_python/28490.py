# 28490
# stuart는 1부터 n까지 번호가 매겨진 n개의 직사각형 프레임을 갖고 있다.
# 프레임 i는 높이 hi와 너비 wi를 갖는 직사각형이다.
# 가장 큰 영역을 덮는 프레임의 크기 구하기

n = int(input())
max = 0

for i in range(n):
    h, w = map(int, input().split(' '))
    cur_result = h * w

    if (cur_result > max):
        max = cur_result

print(max)