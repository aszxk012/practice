# 4458
# 테스트 케이스만큼 문장을 입력받아 문장의 첫번째 문자는 대문자로 변환하여 출력

test = int(input())
result = []

for _ in range(test):
    string = input()
    up = string[0].upper()

    string = string.replace(string[0], up, 1)

    result.append(string)

for i in range(len(result)):
    print(result[i])