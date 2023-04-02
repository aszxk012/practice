# 5355
# @는 x3, %는 +5, #은 -7
# 테스트 케이스 개수가 주어지고 화성수학식이 한 줄에 하나씩 주어지며 소수점 둘째자리까지 출력
# 못 풀었음 > 추후 수정(2023.04.02)

import sys

test = int(input())
result = []

for _ in range(test):
    # 개행문자 > \n 같은 문자 제거 함수 rstrip()
    char = sys.stdin.readline().rstrip()
    cal = char.split(' ')


for i in range(test):
    print(result[i])