# 4470
# 텍스트에서 줄을 입력받은 뒤, 줄 번호를 출력하기

test = int(input())
result = []

for _ in range(test):
    string = input()

    result.append(string)

for i in range(len(result)):
    print(str(i + 1) + ".", result[i])