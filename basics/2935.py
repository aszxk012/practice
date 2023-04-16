# 2935
# 10의 제곱의 수를 입력 받은 후, 연산자 + 또는 *를 입력받는다.
# 다시 10의 제곱의 수를 입력 받은 후에 연산자에 맞는 연산 후 출력

a = int(input())
oper = input()
b = int(input())

if oper == '+':
    print(a + b)
elif oper == '*':
    print(a * b)