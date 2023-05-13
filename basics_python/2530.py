# 2530
# 현재 시각을 입력한 후 요리하는데 필요한 시간이 초 단위로 주어질 때 종료되는 시각 구하기

cur_time = input()
hour, min, sec = cur_time.split(' ')
hour, min, sec = int(hour), int(min), int(sec)

req_time = int(input())

sec = sec + req_time

while sec >= 60:

    if sec >= 60:
        sec -= 60
        min += 1

    if min >= 60:
        min -= 60
        hour += 1

    if hour >= 24:
        hour -= 24

print(hour, min, sec)