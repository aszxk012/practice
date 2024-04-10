# 28281
# N일 뒤는 동원이 생일이다.
# 생일선물로 양말 2X개를 선물하려고 한다. 
# 매일 시장에서 연속 이틀에 걸쳐 양말을 X개씩 살 것이다.
# 오늘부터 i번째 날에 양말 하나에 Ai원이다.
# 최소 비용 출력

import sys

n, x = map(int, input().split(' '))
prices = list(map(int, input().split(' ')))

min = sys.maxsize

for i in range(n - 1):
    cur_sum = prices[i] + prices[i + 1]

    if (min > cur_sum):
        min = cur_sum

total = min * x
print(total)