# 1264
# 모음개수 알려주기

vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
count_vowel = 0
result = []

while True:
    string = input().replace(' ', '')

    if string == '#':
        break

    for i in range(len(string)):
        if string[i] in vowels:
            count_vowel += 1

    result.append(count_vowel)

    count_vowel = 0


for i in range(len(result)):
    print(result[i])