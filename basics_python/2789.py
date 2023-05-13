# 2789
# CAMBRIDGE에 포함된 알파벳은 지우고 출력

cam = "CAMBRIDGE"
result = ""
string = input()

for i in range(len(string)):
    if string[i] in cam:
        pass
    else:
        result += string[i]

print(result)