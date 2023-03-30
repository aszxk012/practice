# 15552
# 더 빠른 속도로 계산하기
# input > sys.stdin.readline
# 문자열 저장하고 싶을 경우: .rstrip()

import sys

count = sys.stdin.readline()
count = int(count)
result = []

for i in range(count):
    num = sys.stdin.readline()
    a, b = num.split(' ')
    a, b = int(a), int(b)

    result.append(a + b)

for i in range(len(result)):
    print(result[i])