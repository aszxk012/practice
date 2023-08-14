# 11319
# 입력받은 테스트 케이스 개수만큼의 문장 안에 자음과 모음 개수 출력
import sys

test = int(input())
vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
count_conson = 0
count_vowel = 0
result = []

for _ in range(test):
    string = input().replace(' ', '')

    for i in range(len(string)):
        if string[i] in vowels:
            count_vowel += 1
        else:
            count_conson += 1

    result.append(count_conson)
    result.append(count_vowel)

    count_conson = 0
    count_vowel = 0

for i in range(0, len(result), 2):
    print(result[i], result[i + 1])