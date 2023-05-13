# 2441
# 첫 줄에는 별 n개, 2번째 줄에는 n - 1개, ... n번째 줄에는 1개 출력
# 오른쪽 정렬

num = int(input())

for i in range(num):
    print(' ' * i + '*' * (num - i))