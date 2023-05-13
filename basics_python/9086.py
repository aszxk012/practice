# 9086
# 테스트 케이스 개수만큼 문자열 입력받아서 문자열의 첫번째와 마지막 문자 출력

test = int(input())
result = []

for _ in range(test):
    string = input()

    result.append(string[0])
    result.append(string[-1])
    
for i in range(0, len(result), 2):
    print(result[i] + result[i + 1])