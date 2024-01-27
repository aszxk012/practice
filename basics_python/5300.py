# 5300
# 정원이 6명인 배에 선원을 태워 보낼 수 있다.
# 마지막으로 출발하는 배는 정원이 다 차지 않아도 출발할 수 있다.
# 선원의 수가 입력으로 주어지며, 배가 출발하는 시점에 "Go!"를 출력한다.

n = int(input())

for i in range(1, n + 1):
    print(i, end=' ')

    if (i % 6 == 0):
        print("Go!", end=' ')

    elif (i == n):
        print("Go!")