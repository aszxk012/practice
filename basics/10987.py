# 10987
# 모음 개수 출력하기

vowels = ['a', 'e', 'i', 'o', 'u']
vowels_count = 0

string = input()

for i in range(len(string)):
    if string[i] in vowels:
        vowels_count += 1

print(vowels_count)