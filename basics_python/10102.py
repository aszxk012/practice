# 10102
# 심사위원 수 입력 받아 누구에게 투표했는지 입력받은 후 누가 이겼는지 출력하기

test = int(input())
vote = input()

a = 0
b = 0

for i in range(len(vote)):
    if vote[i] == 'A':
        a += 1
    else:
        b += 1

if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("Tie")