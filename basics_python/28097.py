# 28097
# N개의 공부 계획 중, i번째 공부 계획을 실행하는 데에 Ti 시간이 소모된다.
# 순서대로 시행하며 계획 사이에는 8시간동안 휴식을 취한다.
# 첫번째 공부 계획을 시작한 시간부터 얼마나 지났는지 며칠 몇 시간 경과되었는지 출력

n = int(input())
plan = list(map(int, input().split(' ')))
time = 0

for i in range(n):
    time += plan[i]

    if ((i + 1) < n):
        time += 8

d = time // 24
h = time % 24

print(d, h)