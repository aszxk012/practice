# 27267
# 미샤의 방은 Am * Bm의 크기고, 페트야의 방은 Cm * Dm의 크기다.
# 미샤의 방이 크면 라틴 문자 M을, 페트야의 방이 더 크면 라틴 문자 P 출력
# 방 크기가 같다면 E 출력
# 둘 중 누구의 방이 더 큰지 출력

a, b, c, d = map(int, input().split(' '))
m = a * b
p = c * d

if (m > p):
    print("M")

elif (m < p):
    print("P")

else:
    print("E")