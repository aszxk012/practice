# 9782
# 중앙값은 정렬된 데이터의 가운데 값이다.
# n개의 데이터가 주어졌을 때, n이 홀수인 경우 중앙값은 (n + 1) / 2번째에 위치하고 있으며
# n이 짝수인 경우 n / 2번째 데이터와 (n / 2) + 1번째 데이터의 평균이다.
# 중앙값을 출력
# 런타임 오류(2024.01.20, 21)

i = 1
while True:
    num_list = list(map(int, input().split(' ')))
    n = num_list[0]
    if (n == 0):
        break
    
    elif (n % 2 == 0):
        temp = n // 2
        median = (num_list[temp] + num_list[temp + 1]) / 2

    elif (n % 2 != 0):
        temp = (n + 1) // 2
        median = num_list[temp]

    print("Case %d: %.1f" % (i, median))
    i += 1