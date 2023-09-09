# 24736
# 미식 축구의 득점 방법은 다섯 가지임.
# 터치 다운 6점, 필드 골 3점, 상대의 자책골 2점, 엑스트라 포인트 1점, 투 포인트 컨버전 2점
# T, F, S, P, C 순으로 입력, (0 <= T <= 10, 0 <= F <= 10, 0 <= S <= 10, 0 <= P + C <= T)
# 두 팀의 박스 스코어가 주어졌을 때 점수 구하기

score_a = list(map(int, input().split(' ')))
score_b = list(map(int, input().split(' ')))

sum_a = 6 * score_a[0] + 3 * score_a[1] + 2 * score_a[2] + 1 * score_a[3] + 2 * score_a[4]
sum_b = 6 * score_b[0] + 3 * score_b[1] + 2 * score_b[2] + 1 * score_b[3] + 2 * score_b[4]

print(sum_a, sum_b)