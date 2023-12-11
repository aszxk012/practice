# 15059
# 첫 번째 줄엔 비행기에 있는 치킨, 소고기, 파스타의 수가 주어지고
# 두 번째 줄엔 치킨, 소고기, 파스타를 주문한 수가 주어질 때
# 원하는 식사를 받지 못하는 손님의 수 출력하기

air_food = list(map(int, input().split(' ')))
order_food = list(map(int, input().split(' ')))
result = 0

for i in range(3):
    if (order_food[i] > air_food[i]):
        result += order_food[i] - air_food[i]

print(result)