# 2525
# 오븐이 끝나는 시간 계산하는 프로그램
# 현재 시간과 오븐 작동 시간을 넣으면 음식이 완료되는 시간을 계산해주는 프로그램

time = input()
timer = input()
hour, min = time.split(' ')
hour, min, timer = int(hour), int(min), int(timer)

hour = hour + (timer // 60)
timer_min = timer % 60
min = min + timer_min

if (min > 59):
    hour += 1
    min -= 60

if (hour > 23):
    hour -= 24


print(hour, min)