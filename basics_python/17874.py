# 17874
# 정사각형 모양의 케이크를 주문했다. 케이크를 가로로 한 번, 세로로 한 번 잘랐다.
# 두 번의 칼질의 결과로 나올 수 있는 가장 큰 케이크 조각의 부피 구하기
# 케이크의 두께는 4cm이며, 정사각형의 한 변의 길이 n,
# 케이크 위쪽 끝에서 가로 칼질까지의 길이 h, 케이크 왼쪽 끝에서 세로 칼질 까지의 길이 v가 주어진다.

n, h, v = map(int, input().split(' '))

h1, h2 = h, (n - h)
v1, v2 = v, (n - v)

max_h = max(h1, h2)
max_v = max(v1, v2)

volume = max_h * max_v * 4

print(volume)