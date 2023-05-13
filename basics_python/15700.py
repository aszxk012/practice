# 15700
# 2x1, 1x2 크기의 타일을 nxm 크기의 벽에 겹치지 않고 최대 몇개 채울 수 있는지 구하기

n, m = map(int, input().split())
nxm = n * m

print(nxm // 2)