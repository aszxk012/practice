# 27959
# 100원 동전을 n개 갖고 있고, 그 돈으로 가격이 m원인 초코바를 살때
# 살 수 있으면 yes를, 살 수 없으면 no 출력하기

n, m = map(int, input().split(' '))
price = n * 100

if price >= m:
    print("Yes")
else:
    print("No")