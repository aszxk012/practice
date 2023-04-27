# 2744
# 대문자는 소문자로, 소문자는 대문자로 바꿔서 출력

string = input()
result = ''

for i in string:
    if i.isupper() == True:
        result += i.lower()
    else:
        result += i.upper()

print(result)