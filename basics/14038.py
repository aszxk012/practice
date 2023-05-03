# 14038
# 선수가 6번의 경기를 치뤘을 때 경기 결과에 따라 속한 그룹 출력
# 5 ~ 6번 이긴 경우: 그룹 1
# 3 ~ 4번 이긴 경우: 그룹 2
# 1 ~ 2번 이긴 경우: 그룹 3
# 한 번도 이기지 못한 경우: 대회에서 탈락 = -1
count_win = 0

for i in range(6):
    result = input()

    if result == 'W':  
        count_win += 1

if count_win >= 5:
    print(1)
elif 5 > count_win >= 3:
    print(2)
elif 3 > count_win >= 1:
    print(3)
else:
    print(-1)