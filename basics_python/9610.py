# 9610
# 좌표 (x, y)가 테스트 개수만큼 주어질 때,
# 각 사분면과 축에 점이 몇개 있는지 구하는 프로그램

test = int(input())
q1_count = 0
q2_count = 0
q3_count = 0
q4_count = 0
axis_count = 0

for _ in range(test):
    x, y = map(int, input().split(' '))

    if (x > 0) and (y > 0):
        q1_count += 1
    elif (x > 0) and (y < 0):
        q4_count += 1
    elif (x < 0) and (y > 0):
        q2_count += 1
    elif (x < 0) and (y < 0):
        q3_count += 1
    else:
        axis_count += 1


print("Q1:", q1_count)
print("Q2:", q2_count)
print("Q3:", q3_count)
print("Q4:", q4_count)
print("AXIS:", axis_count)