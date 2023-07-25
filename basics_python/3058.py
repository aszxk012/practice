# 3058
# 테스트 케이스만큼 7개의 정수 입력받아 짝수의 합과 최솟값 출력하기

import sys

test = int(input())

for _ in range(test):
    nums = map(int, input().split(' '))
    min_num = sys.maxsize
    sum = 0

    for num in nums:
        if num % 2 == 0:
            sum += num
            min_num = min(min_num, num)

    print(sum, min_num)