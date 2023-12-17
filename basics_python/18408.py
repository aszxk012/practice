# 18408
# a, b, c가 1 또는 2로 주어진다.
# 1과 2 중 더 많은 것 출력하기

nums = list(map(int, input().split(' ')))
count_1 = 0
count_2 = 0

for i in range(3):
    if nums[i] == 1:
        count_1 += 1
    elif nums[i] == 2:
        count_2 += 1

if (count_1 > count_2):
    print(1)
else:
    print(2)