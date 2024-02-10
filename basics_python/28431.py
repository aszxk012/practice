# 28431
# 숫자가 쓰여진 양말 5개가 주어진다.
# 같은 숫자가 쓰여진 양말 두 개를 모으면 양말 한 쌍이 된다.
# 쌍을 만들 수 있는 양말을 뺀 후 남은 양말에 쓰인 숫자 출력
# 같은 숫자가 3개인 경우 미해결(2024.02.09, 10)
socks = []
result = []

for _ in range(5):
    cur = int(input())
    socks.append(cur)


for i in range(len(socks)):
    for j in range(i + 1, len(socks)):
        if (socks[i] == socks[j]):
            result.append(socks[i])
            break

for i in range(len(socks)):
    if (not socks[i] in result):
        print(socks[i])
        break