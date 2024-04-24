# 31090
# 각 테스트 케이스에 대해 N + 1이 N의 끝 두자리로 나누어 떨어진다면 Good
# 그렇지 않다면 Bye 출력

n = int(input())

for _ in range(n):
    x = int(input())

    if (((x + 1) % (x % 100) == 0)):
        print("Good")
    else:
        print("Bye")