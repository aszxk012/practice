# 11134
# 쿠키를 N개 가지고 있을 때 며칠 동안 먹을 수 있는지 출력하기

test = int(input())

for _ in range(test):
    cookie, eating = map(int, input().split(' '))

    days = (cookie // eating)
    
    if (cookie % eating != 0):
        days += 1
        
    print(days)
