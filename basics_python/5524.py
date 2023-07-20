# 5524
# 문자열 입력받아 모두 소문자로 변환하여 출력하기

test = int(input())
result = []


for i in range(test):
    string = input()
    result.append(string)
    
for i in range(test):
    result[i] = result[i].lower()
    print(result[i])