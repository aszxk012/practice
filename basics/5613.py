# 5613
# 덧셈, 뺄셈, 곱셈, 나눗셈을 할 수 있는 계산기 프로그램
# 추후 수정(2023.05.03)
# 수정 완료(2023.05.04)

calcul = []
result = 0

while True:
    string = input()

    if string == '=':
        break
    else:
        calcul.append(string)

# 문자열인 정수 타입 정수로 바꾸기
for i in range(len(calcul)):
    if calcul[i].isdigit() == True:
        calcul[i] = int(calcul[i])

result += calcul[0]
for i in range(1, len(calcul), 2):
    if calcul[i] == '+':
        result += calcul[i + 1]

    elif calcul[i] == '-':
        result -= calcul[i + 1]
            
    elif calcul[i] == '*':
        result *= calcul[i + 1]
        
    elif calcul[i] == '/':
        result = int(result / calcul[i + 1])

print(int(result))