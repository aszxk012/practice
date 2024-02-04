# 8710
# 코직의 키, 코치가 요구한 키, 한 번 때릴 때마다 늘어나는 혹의 길이가 주어진다.
# 몇 번을 때려야하는지 출력

h, w, m = map(int, input().split(' '))
diff = w - h
hit = diff // m

if (diff % m != 0):
    hit += 1

print(hit)