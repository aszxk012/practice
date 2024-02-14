# 28648
# n개의 버스 시간이 주어진다.
# t는 버스가 집을 지나가는 데 걸리는 시간, s는 집에서 쇼핑센터까지 걸리는 시간이다.
# 최소 시간 출력

import sys

n = int(input())
bus_a, bus_b = [], []

for _ in range(n):
    a, b = map(int, input().split(' '))
    bus_a.append(a)
    bus_b.append(b)

total = sys.maxsize

for i in range(n):
    cur_total = bus_a[i] + bus_b[i]

    if (cur_total < total):
        total = cur_total
    
print(total)