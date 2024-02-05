# 24196
# 암호화된 메세지 복호화
# 입력 문자열의 첫 번째 문자는 출력 문자열에 포함
# 출력 문자열에 포함된 각 문자는 입력 문자열에서 다음에 포함될 문자의 위치를 나타냄
# ex) "A"는 다음 문자가 한 위치 뒤에 있음, "B"는 다음 문자가 두 위치 뒤에 있음 ...
# 입력의 마지막 문자에 도달하면 해당 문자를 출력 문자열에 포함한 뒤 작업 완료

string = input().upper()
output = ""
space = 0

for i in range(len(string)):
    if (i == 0):
        output += string[i]
        ascii = ord(string[i]) - 64
        space = ascii

    else:
        if (space != 1):
            space -= 1

        else:
            output += string[i]
            ascii = ord(string[i]) -64
            space = ascii
            
print(output)