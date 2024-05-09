# 27918
# 달구와 포닉스는 탁구 치는 것을 좋아한다. 누가 경기에서 승리할지 예측해보자.
# 처음에 달구와 포닉스는 점수 0점을 가지고 시작한다. 각 라운드에서 이긴사람이 1점 얻는다.
# n회의 라운드가 모두 끝나거나 경기 진행 도중 누군가가 2점 앞서게 되면 경기가 종료된다.
# 몇 대 몇으로 끝나는지 출력

n = int(input())
d_score, p_score = 0, 0

for i in range(n):
    winner = input()

    diff = abs(d_score - p_score)

    if (diff < 2):
        if (winner == "D"):
            d_score += 1
        elif (winner == "P"):
            p_score += 1
    
    else:
        continue

print("%d:%d" % (d_score, p_score))