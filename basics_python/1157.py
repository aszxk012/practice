# 1157
# 문자열이 주어졌을 때, 가장 많이 사용된 알파벳 출력하기
# 대문자, 소문자 구분 X
# 여러 개인 경우 ? 출력
# 여러 개인 경우 ? 출력 불가능(2023.08.03)

import sys

string = input().upper()
string_list = [char for char in string]

# 중복 제거
alphabet = set(string_list)
alphabet = list(alphabet)

count = []

for _ in range(len(alphabet)):
    count.append(0)
    
for i in range(len(string)):
    if string[i] in alphabet:
        
        for j in range(len(count)):
            if string[i] == alphabet[j]:
                count[j] += 1
                
print(alphabet)
print(count)
max = -sys.maxsize - 1
max_char = ''

for i in range(len(alphabet)):
    if (count[i] > max):
        max = count[i]
        max_char = alphabet[i]

print(max_char)