# 15873
# 공백 없이 두 수가 주어질때, A + B 출력하기
# 0 < A, B <= 10

nums = input()

if nums[1] == "0":
    a = int(nums[:2])
    b = int(nums[2:])
else:
    a = int(nums[:1])
    b = int(nums[1:])

print(a + b)