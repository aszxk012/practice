# 30008
# 학생수 N과 과목 수 K, 다음 줄에 등수가 주어진다.
# N명의 학생과 K개의 과목이 있으며 모든 학생은 K개의 과목을 전부 수강한다.
# 등급은 백분율을 기준으로 부여되며 백분율은 등수에 100을 곱한 뒤 학생수로 나눈 몫이다.
# 등급 출력

n, k = map(int, input().split(' '))
rank = list(map(int, input().split(' ')))
p = []

for i in range(k):
    score = rank[i]
    percent = score * 100 // n

    if (0 <= percent <= 4):
        p.append(1)
    elif (4 < percent <= 11):
        p.append(2)
    elif (11 < percent <= 23):
        p.append(3)
    elif (23 < percent <= 40):
        p.append(4)
    elif (40 < percent <= 60):
        p.append(5)
    elif (60 < percent <= 77):
        p.append(6)
    elif (77 < percent <= 89):
        p.append(7)
    elif (89 < percent <= 96):
        p.append(8)
    else:
        p.append(9)

for i in range(k):
    print(p[i], end=' ')