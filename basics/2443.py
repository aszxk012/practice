# 2443
# 첫째 줄에는 별 2×N-1개, 둘째 줄에는 별 2×N-3개, ..., N번째 줄에는 별 1개 찍기
# 가운데 대칭

num = int(input()) + 1

for i in range(1, num, 1):
    print(" " * (i - 1) + "*" * ((num - i) * 2 - 1))