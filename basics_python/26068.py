# 26068
# 선물받은 횟수와 선물의 남은 유효기간이 주어진다.
# 유효기간이 90일 이하로 남은 기프티콘을 사용한다고 할 때 사용할 기프티콘의 개수 출력

n = int(input())
count = 0

for _ in range(n):
    string = input()
    day = string[2:]
    day = int(day)

    if (day <= 90):
        count += 1

print(count)