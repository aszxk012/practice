# 11945
# 오류 미수정(2023.07.27)

n, m = map(int, input().split(' '))
fish = []
result = []

for i in range(n):
    cur = input()
    fish.append(cur)

    for j in range(m):
        string = fish[i]
        fish[i] = string[::-1]

for i in range(n - 1, -1, -1):
    print(fish[i])
