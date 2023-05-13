# 5355
# @는 x3, %는 +5, #은 -7
# 테스트 케이스 개수가 주어지고 화성수학식이 한 줄에 하나씩 주어지며 소수점 둘째자리까지 출력
# 못 풀었음 > 추후 수정(2023.04.02)

test = int(input())
temp_num = 0
result = []

for _ in range(test):
    char = input()
    char_split = char.split(' ')

    temp_num = float(char_split[0])
    del char_split[0]

    oper = char_split
    
    for i in oper:
        if i == "@":
            temp_num = temp_num * 3

        elif i == "#":
            temp_num = temp_num - 7
    
        elif i == "%":
            temp_num = temp_num + 5

    result.append(temp_num)


for i in range(test):
    print("%.2f"%result[i])