# 5928
# 11월 11일 11시 11분에 문제를 다운로드 받아 풀기 시작한다고 했을 때,
# 문제를 다 푼 일, 시간, 분이 주어진다.
# 투자한 시간을 분으로 출력한다. 다 푼 시간이 문제를 풀기 시작한 시간보다 빠를 때, -1 출력
# 오답 추후 수정(23.12.05, 06)

date = 111111
d, h, m = map(int, input().split(' '))
input_date = d * 10000 + h * 100 + m
min_time = (11 * 24 * 60) + (11 * 60) + 11

if (input_date < date):
    print(-1)

else:
    input_time = (d * 24 * 60) + (h * 60) + m
    print(input_time - min_time)