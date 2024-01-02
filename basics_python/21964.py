# 21964
# 공백이 없는 문자열이 주어질 때, 마지막 5글자만 출력하기

n = int(input())

if (n >= 5):
    string = input()
    temp = n - 5
    print(string[temp::])
