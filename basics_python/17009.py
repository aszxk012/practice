# 17009
# 첫 세줄은 팀 사과의 득점, 다음 세줄은 팀 바바나의 득점
# 세줄은 순서대로 3점 슛 성공 횟수, 2점 슛 성공 횟수, 1점 자유투 성공 횟수
# 각 숫자는 0 ~ 100 사이의 수
# 팀 사과의 점수가 높은 경우 "A"를, 팀 바나나가 높은 경우 "B"를, 무승부인 경우 "T" 출력

team_a = []
team_b = []
result_a = 0
result_b = 0

for i in range(3):
    a = int(input())
    team_a.append(a)

for i in range(3):
    b = int(input())
    team_b.append(b)

result_a = team_a[0] * 3 + team_a[1] * 2 + team_a[2]
result_b = team_b[0] * 3 + team_b[1] * 2 + team_b[2]

if result_a > result_b:
    print("A")
elif result_a < result_b:
    print("B")
else:
    print("T")