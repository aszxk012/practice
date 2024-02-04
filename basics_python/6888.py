# 6888
# 시장은 4년마다, 재무는 2년마다, 수석 프로그래머는 3년마다, 개잡이는 5년마다 바뀐다.
# X년, 모든 위치가 변경되었다. 미래 Y년이 주어질 때 모든 직위가 변경되는 시기를 나열한다.

x = int(input())
y = int(input())
temp = x

while (temp <= y):
    print("All positions change in year", temp)
    temp += 60
