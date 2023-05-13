# 3046
# s = (r1 + r2) / 2
# r1, s를 알고 있을 때 r2 구하기

nums = input()
r1, s = nums.split(' ')
r1, s = int(r1), int(s)

r2 = 2 * s - r1

print(r2)