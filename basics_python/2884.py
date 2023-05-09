# 2884
# 45분 빠른 시계의 시간 구하기

time = input()
hour, min = time.split(' ')
hour, min = int(hour), int(min)

min = min - 45

if (min < 0):
    hour -= 1
    min = min + 60

    if (hour < 0):
        hour = hour + 24

print(hour, min)