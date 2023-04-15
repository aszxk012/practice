# 2752
# 세 수 입력받아 오름차순으로 정렬하기


def Sort(num1, num2, num3):
    nums = [num1, num2, num3]

    max_num = max(nums)
    
    if max_num == num1:
        del nums[0]
    elif max_num == num2:
        del nums[1]
    elif max_num == num3:
        del nums[2]

    if nums[0] > nums[1]:
        mid_num = nums[0]
        min_num = nums[1]
    else:
        mid_num = nums[1]
        min_num = nums[0]
    
    return min_num, mid_num, max_num

a, b, c = map(int, input().split(' '))
min_num, mid_num, max_num = Sort(a, b, c)
print(min_num, mid_num, max_num)