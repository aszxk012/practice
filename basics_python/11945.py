# 11945
# 오류 미수정(2023.07.27) > 오류 수정(2023.08.01)

n, m = map(int, input().split(' '))
fish = []
result = []

for i in range(n):
    fish.append(input())
    
for i in range(n):
    for j in range(m - 1, -1, -1):
        result.append(fish[i][j])
        
for i in range(n * m):
    print(result[i], end='')
    
    if ((i + 1) % m == 0):
        print()
