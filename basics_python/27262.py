# 27262
# 미샤는 n층에 산다. 엘리베이터는 k층에 있으며 미샤는 1층에 서있다.
# 한 층을 계단으로 올라가는 데에 a초, 엘리베이터는 한 층당 b초가 걸린다.
# 각각 걸리는 시간 출력

n, k, a, b = map(int, input().split(' '))
steps = (n - 1) * a
elev = ((k - 1) * b) + ((n - 1) * b)

print(elev, steps)