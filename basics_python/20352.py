# 20352
# 서커스 천막의 넓이가 주어질 때 이 텐트의 둘레를 m 단위로 출력

import math

s = float(input())
pi = math.pi
r = math.sqrt(s / pi)
l = 2 * pi * r

print(l)