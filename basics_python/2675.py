# 2675
# 문자열 s를 입력 받은 후 첫번째 문자를 r번, 두번째 문자를 r번 반복하는 식으로 새 문자열 p를 만든다.
# 문자 단위로 줄바꿈해서 출력됨 > 추후 수정(2023.04.02)
# 수정 완료(2023.04.21)

test = int(input())
result = []
string = ''


for _ in range(test):
    tot_string = input()

    num, char = tot_string.split(' ')
    num = int(num)

    for i in range(len(char)):
        string += char[i] * num
        
    result.append(string)
    string = ''

for i in range(len(result)):
    print(result[i])