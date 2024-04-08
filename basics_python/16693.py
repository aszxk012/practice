# 16693
# 조각피자 A1 넓이의 가격 P1, 원형 피자 R1 반지름에 가격 P2
# 어느 피자를 구매하는 것이 나은지 출력하기
# 오답 추후 수정(23.12.13, 14, 15) > 정답(24.02.12)

import math

a, p1 = map(int, input().split(' '))
r, p2 = map(int, input().split(' '))

a_area = a / p1
b_area = math.pi * r * r / p2

if (a_area <= b_area):
    print("Whole pizza")

else:
    print("Slice of pizza")