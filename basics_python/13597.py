# 13597
# 1 ~ 13 정수
# 같은 수 3개 > 같은 수 2개
# 더 큰 수 3개 > 같은 수 3개
# 더 큰 수 2개 > 같은 수 2개
# 두 정수를 입력 받고 승리할 확률을 최대로 만드는 정수의 값 출력하기

a, b = map(int, input().split(' '))

if a == b:
    print(a)
elif a > b:
    print(a)
else:
    print(b)