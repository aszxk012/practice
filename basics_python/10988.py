# 10988
# 팰린드롬: 앞으로 읽어도, 거꾸로 읽어도 같은 단어일 때
# 팰린드롬 판별하기

char = input()
char_oppo = ''
palindrome = 0

for i in char:
    char_oppo = i + char_oppo

for i in range(len(char_oppo)):
    if char_oppo[i] == char[i]:
        palindrome = 1
    else:
        palindrome = 0
        break

print(palindrome)