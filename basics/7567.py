# 7567
# 그릇의 높이는 10cm, 같은 방향이면 +5cm, 다른 방향이면 +10cm

bowl = input()
height = 0

for i in range(len(bowl)):
    if i == 0:
        height += 10

    elif bowl[i - 1] != bowl[i]:
        height += 10
    
    elif bowl[i - 1] == bowl[i]:
        height += 5

print(height)