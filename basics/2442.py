# 2442
# 첫째 줄에는 별 1개, 둘째 줄에는 별 3개, ..., N번째 줄에는 별 2×N-1개 찍기
# 가운데 대칭

test = int(input())

for i in range(1, test + 1, 1):
    star_loop_num = (2 * i) - 1
    space_loop_num = test - i
    print(" " * space_loop_num + "*" * star_loop_num)