# 25600
# a, d, g는 애드혹, 다이내믹 프로그래밍, 그리디 알고리즘 문제 해결을 통해 얻은 점수이다.
# 총점 계산은 a * (d + g)로 계산하며 a = (d + g)인 경우 원래 점수의 두 배로 계산한다.
# 가장 높은 점수 출력

n = int(input())
max_score = 0

for _ in range(n):
    a, d, g = map(int, input().split(' '))

    total = a * (d + g)
    condition = d + g

    if (a == condition):
        total *= 2
    
    if (total > max_score):
        max_score = total
    
print(max_score)