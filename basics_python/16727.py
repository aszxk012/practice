# 16727
# 두 팀의 점수 p1, s1와 s2, p2가 주어진다.
# 합계 점수를 구하여 우승 팀("Persepolis 또는 Esteghlal") 출력하고
# 동점이라면 원정에서 더 많은 점수를 얻은 팀이 우승이고, 그 점수도 같다면 "Penalty" 출력하기

p1, s1 = map(int, input().split(' '))
s2, p2 = map(int, input().split(' '))

s = s1 + s2
p = p1 + p2

if (s > p):
    print("Esteghlal")
elif (s < p):
    print("Persepolis")
else:
    if (s1 < p2):
        print("Persepolis")
    elif (s1 > p2):
        print("Esteghlal")
    else:
        print("Penalty")