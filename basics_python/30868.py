# 30868
# 모든 후보자는 0표, 아무것도 그려져 있지 않는 상태로 시작한다.
# 어떤 후보자가 한 표를 받을 때마다 |를 맨 뒤에 그린다.
# 그 후보자가 5표를 받을 때마다 |를 그리는 대신 ++++를 만든 후 한 칸의 공백을 추가한다.

n = int(input())
vote_5 = "++++ "
vote_1 = "|"

for _ in range(n):
    vote = ""
    vote_num = int(input())

    cur_vote_5 = vote_num // 5
    cur_vote_1 = vote_num % 5

    if (cur_vote_5 > 0):
        vote += vote_5 * cur_vote_5
    
    if (cur_vote_1 > 0):
        vote += vote_1 * cur_vote_1

    print(vote)