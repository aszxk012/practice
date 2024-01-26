# 25191
# 치킨 1마리를 먹을 때 집에 있는 콜라 2개나 맥주 1개와 같이 먹어야 한다.
# 치킨집에 있는 치킨의 개수보다 치킨을 많이 시켜먹을 수 없다.
# 치킨 집에 있는 치킨의 개수와 집에 있는 콜라, 맥주의 개수가 주어질 때
# 시켜먹을 수 있는 치킨의 총 개수 출력

chicken = int(input())
coke, beer = map(int, input().split(' '))

total = int(coke / 2) + beer

if (total > chicken):
    total = chicken

print(total)