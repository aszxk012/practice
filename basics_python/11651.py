# 11651
# 테스트 케이스만큼 좌표 입력받아 y좌표를 오름차순으로 정렬
# y좌표가 같다면 x좌표를 오름차순으로 정렬하기
# 추후 수정(2023.08.05)

test = int(input())
xy = []
x = []
y = []
result = []

for i in range(test):
    x, y = map(int, input().split(" "))
    xy.append(x)
    xy.append(y)

y = y.sort()
print(y)

for i in range(len(result)):
    print(result[i])