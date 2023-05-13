# 2163
# 1 x 1 크기의 초콜릿 쪼갤 때 N x M 크기의 초콜릿으로 만들기 위한 최소 쪼개기 횟수 구하기
# ex) 2 x 2는 3번 쪼개야 함

nums = input()
n, m = nums.split(' ')
n, m = int(n), int(m)

print(n * m - 1)