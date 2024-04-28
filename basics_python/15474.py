# 15474
# 세트 X는 A개에 B엔, 세트 Y는 C개에 D엔일 때
# 연필 N개를 구매할 수 있는 최소 금액 출력하기
# 시간초과 추후 수정(23.12.11, 24.02.11) > 해결(2024.04.28.)

n, a, b, c, d = map(int, input().split(' '))
X_set = n // a
Y_set = n // c

if (n % a != 0):
    X_set += 1

if (n % c != 0):
    Y_set += 1

final = min(X_set * b, Y_set * d)
print(final)