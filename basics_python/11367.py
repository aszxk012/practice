# 11367
# 테스트 케이스 입력받아서 이름과 점수를 이름과 등급으로 출력하기

def Grade(score):
    if 97 <= score:
        grade = 'A+'
    elif 90 <= score < 97:
        grade = 'A'
    elif 87 <= score < 90:
        grade = 'B+'
    elif 80 <= score < 87:
        grade = 'B'
    elif 77 <= score < 80:
        grade = 'C+'
    elif 70 <= score < 77:
        grade = 'C'
    elif 67 <= score < 70:
        grade = 'D+'
    elif 60 <= score < 67:
        grade = 'D'
    else:
        grade = 'F'


    return grade

test = int(input())

result = []
for i in range(test):
    name, score = input().split(' ')
    grade = Grade(int(score))

    result.append(name)
    result.append(grade)

for i in range(0, len(result), 2):
    print(result[i], result[i + 1])