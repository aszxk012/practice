# 16693
# 조각피자 A1 넓이의 가격 P1, 원형 피자 R1 반지름에 가격 P2
# 어느 피자를 구매하는 것이 나은지 출력하기
# 오답 추후 수정(23.12.13)

a, p1, r, p2 = map(int, input().split(' '))

b = 3.14 * r * r

if (a > b):
    if (p1 <= p2):
        print("Slice of pizza")
else:
    if (p1 >= p2):
        print("Whole pizza")