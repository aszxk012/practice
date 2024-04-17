# 31306
# 주어진 문자열에서 y가 모음이라고 가정할 때의 모음 개수, 아니라고 가정할 때의 모음 개수 출력
# 모음이 아니라고 가정했을 때, 맞다고 가정했을 때의 순서대로 출력

string = input()
vowel = ['a', 'e', 'i', 'o', 'u']
not_y, yes_y = 0, 0

for i in string:
    if (i in vowel):
        not_y += 1
        yes_y += 1
    
    if (i == 'y'):
        yes_y += 1

print(not_y, yes_y)