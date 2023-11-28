# 29731
'''Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna stop'''
# 하나라도 위의 문장이 아니라면 Yes 출력, 맞다면 No 출력

strings = ["Never gonna give you up", "Never gonna let you down", "Never gonna run around and desert you",
           "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you", "Never gonna stop"]

n = int(input())
flag = 0
for i in range(n):
    string = input()

    if string in strings:
        flag += 1
    else:
        flag -= 1

if flag == n:
    print("No")
else:
    print("Yes")