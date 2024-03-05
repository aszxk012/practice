# 18414
# 정수 x, l, r이 주어질 때, l이상 r이하의 정수 중 x와의 차의 절댓값이 가장 작은 것 출력

import sys

x, l, r = map(int, input().split(' '))
result = 0
min = sys.maxsize

for i in range(l, r + 1, 1):
    cur = abs(x - i)

    if (cur < min):
        min = cur
        result = i

print(result)