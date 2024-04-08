# 27110
# 후라이드, 간장, 양념치킨을 각각 N마리씩 주문하였고 1인당 치킨을 한마디씩 배부하려 한다.
# 치킨 종류 선호도를 조사했고, 후라이드, 간장, 양념 각각 A명, B명, C명인 것을 알아냈다.
# 한 종류의 치킨만 답했다고 가정할 때, 본인이 가장 선호라는 종류의 치킨을 받을 수 있는 인원의 최댓값 출력

n = int(input())
a, b, c = map(int, input().split(' '))
result = 0

if (a <= n):
    result += a
else:
    result += n

if (b <= n):
    result += b
else:
    result += n

if (c <= n):
    result += c
else:
    result += n

print(result)