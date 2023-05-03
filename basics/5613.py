# 5613
# 덧셈, 뺄셈, 곱셈, 나눗셈을 할 수 있는 계산기 프로그램
# 추후 수정(2023.05.03)

calcul = []

while True:
    string = input()

    if string == '=':
        break

    elif string.isdigit() == True:
        num = int(string)

        calcul.append(num)
    
    calcul.append(string)

result = 0

for i in range(len(calcul)):
    if result == 0:
        if calcul[i] == '+':
            reuslt = int(calcul[i - 1]) + int(calcul[i + 1])

        elif calcul[i] == '-':
            result = int(calcul[i - 1]) - int(calcul[i + 1])
            
        elif calcul[i] == '*':
            result = int(calcul[i - 1]) * int(calcul[i + 1])
        
        elif calcul[i] == '/':
            result = int(calcul[i - 1]) / int(calcul[i + 1])

    else:
        if calcul[i] == '+':
            reuslt += calcul[i + 1]

        elif calcul[i] == '-':
            result -= calcul[i + 1]
            
        elif calcul[i] == '*':
            result *= calcul[i + 1]
        
        elif calcul[i] == '/':
            result = result / calcul[i + 1]


print(int(result))