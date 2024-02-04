# 27213
# m * n 사이즈의 모눈 종이 가장자리만 칠했을 때
# 몇 칸을 칠했는 지 출력하기

m = int(input())
n = int(input())

side = 0

if ((m < 3) or (n < 3)):
    side = m * n
else:
    side = 2 * (m + n) - 4

print(side)