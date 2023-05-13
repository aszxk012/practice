# 20332
# 세 명의 팀원이 받는 상금의 양은 모두 같아야한다.
# 세 팀원이 상금을 동등하게 나눌 수 있으면 yes, 아니면 no 출력

contest = int(input())
prize = list(map(int, input().split(' ')))
total = 0

for i in range(len(prize)):
    total += prize[i]

if total % 3 == 0:
    print("yes")
else:
    print("no")