# 25858
# 학생들이 각가 푼 문제 수에 비례하게 상금을 분배한다.
# 팀원 수를 나타내는 n과 상금 d가 주어지고
# 학생 수만큼 학생들이 해결한 문제의 수가 주어진다.
# 받을 상금 출력

n, d = map(int, input().split(' '))
solve = []
total = 0

for _ in range(n):
    solve_std = int(input())
    total += solve_std
    solve.append(solve_std)

cash = d / total

for i in range(n):
    result = int(solve[i] * cash)
    print(result)