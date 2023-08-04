# 1157
# 문자열이 주어졌을 때, 가장 많이 사용된 알파벳 출력하기
# 대문자, 소문자 구분 X
# 여러 개인 경우 ? 출력
# 여러 개인 경우 ? 출력 불가능(2023.08.03) > 수정(2023.08.04)

string = input().upper()
alphabet = list(set(string))

count_list = []
    
for i in alphabet:
    count = string.count(i)
    count_list.append(count)

if count_list.count(max(count_list)) > 1:
    print("?")
else:
    index = count_list.index(max(count_list))
    print(alphabet[index])