# 31612
# 길이 N의 문자열 S가 주어진다. S의 각 문자는 j, o, i 중 하나다.
# j의 화수는 2, o의 화수는 1, i의 화수는 2일 때 문자열의 총 화수 출력

n = int(input())
s = input()
result = 0

for i in s:
    if (i == 'j'):
        result += 2
    elif (i == 'o'):
        result += 1
    elif (i == 'i'):
        result += 2

print(result)