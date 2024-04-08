# 9782
# 중앙값은 정렬된 데이터의 가운데 값이다.
# n개의 데이터가 주어졌을 때, n이 홀수인 경우 중앙값은 (n + 1) / 2번째에 위치하고 있으며
# n이 짝수인 경우 n / 2번째 데이터와 (n / 2) + 1번째 데이터의 평균이다.
# 중앙값을 출력
# 런타임 오류(2024.01.20, 21, 02.13, 03.11, 03.30)

i = 1
while True:
    num_list = list(map(int, input().split(' ')))
    if (num_list[0] == 0):
        break
    
    n, num_list = num_list[0], num_list[1:]
    
    if (n % 2 == 0):
        median = (num_list[n // 2 - 1] + num_list[n // 2]) / 2

    elif (n % 2 != 0):
        median = num_list[(n + 1) // 2 - 1]

    print("Case %d: %.1f" % (i, median))
    i += 1

# -----------------------------------
T = 0
while True :
    data = [*map(int, input().split())]
    if data[0] == 0 : break
    T += 1
    N, D = data[0], data[1:]
    print("Case %d: %.1f" %( T, D[(N + 1) // 2 - 1] if N % 2 else (D[N // 2 - 1] + D[(N // 2)]) / 2) )