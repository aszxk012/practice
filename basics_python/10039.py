# 10039
# 평균 점수 구하기

sum = 0

for i in range(5):
    grade = int(input())

    if grade < 40:
        grade = 40

    sum += grade

avg = int(sum / 5)

print(avg)