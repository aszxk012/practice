# 26531
# 식이 주어질 때 참이면 "YES", 아니면 "NO" 출력

string = input().split(' ')
a, b, c = int(string[0]), int(string[2]), int(string[-1])
sum = a + b

if (sum == c):
    print("YES")
else:
    print("NO")