# 26546
# 문자열과 i, j가 주어진다.
# i는 제거할 부분 문자열의 시작 인덱스이며, j-1까지 제거한다.
# 제거된 부분 문자열의 길이는 j-i이며 제거한 후의 문자열을 출력한다.

n = int(input())

for i in range(n):
    string, i, j = input().split(' ')
    i, j = int(i), int(j)

    substr = string[i:j]
    result = string.replace(substr, "")
    print(result)