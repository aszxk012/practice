# 31654
# 공백을 간격으로 A, B, C 세 정수가 주어진다.
# A + B = C를 만족하면 correct!를, 아니면 wrong! 출력

a, b, c = map(int, input().split(' '))
sum = a + b

if (sum == c):
    print("correct!")
else:
    print("wrong!")