# 31609
# 0 이상 9 이하의 정수로 이루어진 길이 N의 수열이 주어진다.
# 수열에 적어도 1번 나타나는 정수를 모두 작은 순서대로 출력
# set()은 정렬을 보장하지 않음

n = int(input())
nums = list(map(int, input().split(' ')))
nums = set(nums)
nums = sorted(nums)

for num in nums:
    print(num)