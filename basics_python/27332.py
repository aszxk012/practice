# 27332
# 두 개의 정수 a, b가 주어질 때
# 2022년 11월 a일의 b주일 후가 2022년 11월이면 1을, 아니면 0 출력
# x 주일 후의 날짜는 7 * x일 후를 의미한다.

a = int(input())
b = int(input())

sum = a + (b * 7)

if (sum > 30):
    print(0)
else:
    print(1)