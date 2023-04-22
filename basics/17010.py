# 17010
# 테스트 개수 입력받아 양수와 문자 입력받아 숫자만큼 문자 반복 출력

test = int(input())
string = ''
result = []

for _ in range(test):
    num, char = input().split(' ')
    num = int(num)

    for i in range(num):
        string += char
    result.append(string)
    string = ''

for string in result:
    print(string)