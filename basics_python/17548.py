# 17548
# 대화 상대가 he..ey로 시작 인사를 했다면 당신도 마찬가지로 hee..eey로 인사해야한다.
# 대신 e가 두 배 더 많이 들어가야한다고 할 때, 대답 인사말 출력

greeting = input()
answer = ""
e_num = 0

for i in greeting:
    if (i == 'e'):
        e_num += 1
    
answer += "h"
answer += "e" * (e_num * 2)
answer += "y"

print(answer)