# 13985
# a + b = c 형태의 입력이 들어올 때
# 해당 수식이 참이면 YES를, 거짓이면 NO 출력

sentence = list(input().split(' '))
a = int(sentence[0])
b = int(sentence[2])
c = int(sentence[-1])
sum = a + b

if (sum == c):
    print("YES")
else:
    print("NO")