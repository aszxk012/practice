# 10821
# 숫자와 콤마로만 이루어진 문자열이 주어질 때
# 문자열 안에 포함되어 있는 정수의 개수 출력

string = list(input().split(','))
count = 0

for num in string:
    if num.isdigit():
        count += 1
        
print(count)