# 5928
# 11월 11일 11시 11분에 문제를 다운로드 받아 풀기 시작한다고 했을 때,
# 문제를 다 푼 일, 시간, 분이 주어진다.
# 투자한 시간을 분으로 출력한다. 다 푼 시간이 문제를 풀기 시작한 시간보다 빠를 때, -1 출력
# 오답 추후 수정(23.12.15, 16)

date = 111111
d, h, m = map(int, input().split(' '))
input_date = d * 10000 + h * 100 + m

if (input_date < date):
    print(-1)

else:
    d -= 11
    h -= 11
    m -= 11

    if (h < 0):
        d -= 1
        h += 60

    if (d > 0):
        h += d * 24
        m += h * 60

        print(m)
    else:
        m += h * 60
        print(m)