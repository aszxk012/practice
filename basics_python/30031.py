# 30031
# 지폐의 세로는 68mm로 모두 같지만 가로 길이는 모두 다르다.
# 지폐 N장의 크키가 주어질 때 총 금액 출력

money = {136 : 1000, 142 : 5000, 148 : 10000, 154 : 50000}
n = int(input())
total = 0

for i in range(n):
    w, h = map(int, input().split(' '))
    cur = money[w]

    total += cur
    
print(total)