# 28431
# 숫자가 쓰여진 양말 5개가 주어진다.
# 같은 숫자가 쓰여진 양말 두 개를 모으면 양말 한 쌍이 된다.
# 쌍을 만들 수 있는 양말을 뺀 후 남은 양말에 쓰인 숫자 출력
# 같은 숫자가 3개인 경우 미해결(2024.02.09, 10) > 해결(2024.04.18.)

socks = []

for _ in range(5):
    cur = int(input())
    socks.append(cur)

for i in range(5):
    for j in range(i + 1, 5):
        if socks[i] == socks[j]:
            socks[i] = socks[j] = None
            break

for sock in socks:
    if sock is not None:
        print(sock)
        break