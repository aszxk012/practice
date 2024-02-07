# 26560
# 입력될 문장의 수가 주어지고 문장이 주어진다.
# 문장의 끝에 마침표(.)이 찍혀있을 수도, 없을 수도 있다.
# 문장 끝에 마침표를 포함하여 출력

n = int(input())

for _ in range(n):
    string = input()

    if (string[-1] != '.'):
        string += '.'
    
    print(string)