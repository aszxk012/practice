# 10822
# 문자열이 주어질 때, 문자열에 포함되어 있는 자연수의 합 구하기

nums = list(input().split(','))
sum = 0

for i in nums:
    s = int(i)
    sum += s

print(sum)