# 10599
# a, b는 출생일 범위, c, d는 사망일 범위일 때 최소 나이와 최대 나이 출력하기
# a, b, c, d 입력이 모두 0일 경우 종료

while True:
    a, b, c, d = map(int, input().split(' '))
    if (a == 0 and b == 0 and c == 0 and d == 0):
        break
    
    min_birth = min(a, b)
    max_birth = max(a, b)

    min_death = min(c, d)
    max_death = max(c, d)

    min_age = min_death - max_birth
    max_age = max_death - min_birth

    print(min_age, max_age)