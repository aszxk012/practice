# 2439
# 1번째 줄엔 1개, 2번째 줄엔 2개, n번째 줄엔 n개 별 찍기
# 오른쪽 정렬

count = int(input())

for i in range(count):
    print(" " * (count - (i + 1)) + "*" * (i + 1))