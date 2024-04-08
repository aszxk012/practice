# 27880
# 숭실대학교역의 깊이를 cm단위로 출력, 깊이는 출구에서 플랫폼까지의 수직 거리임.
# 계단: 1층에서 x개의 계단을 내려가면 2층에 도착함.
# 에스컬레이터: 1층에서 x개의 계단을 내려가면 2층에 도착함.
# 에스컬레이터의 한 계단 높이는 21cm이며, 계단의 한 칸 높이는 17cm이다.

total = 0
for i in range(4):
    method, steps = input().split(' ')
    steps = int(steps)

    if (method == 'Es'):
        total += 21 * steps
    
    elif (method == 'Stair'):
        total += 17 * steps

print(total)