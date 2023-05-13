# 5717
# 남자친구와 여자친구 수 입력받아 친구가 총 몇명인지 구하기
# 입력 마지막 줄에는 0 두 개

result = []

while True:
    m, f = map(int, input().split(' '))

    if m == 0 and f == 0:
        break

    result.append(m + f)

for i in range(len(result)):
    print(result[i])