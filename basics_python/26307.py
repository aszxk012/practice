# 26307
# 오후 9시 정각에 문제를 풀기 시작하여 H시 M분에 정답을 맞췄다.
# H와 M이 주어질 때 정답을 맞추기 까지 걸린 시간을 분 단위로 출력하기

h, m = map(int, input().split(' '))
h = h - 9

time = h * 60 + m

print(time)