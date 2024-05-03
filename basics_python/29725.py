# 29725
# 체스판 기물 점수는 백의 기물 점수 합에서 흑의 기물 접수 합을 뺀 값이다.
# 킹, 폰, 나이트, 비숍, 룩, 퀸의 기물 점수는 각각 0, 1, 3, 3, 5, 9점이다.
# 체스판 기물 점수 출력(백의 기물은 대문자, 흑의 기물은 소문자)
# .: 빈칸, K, k: 킹, P, p: 폰, N, n: 나이트, B, b: 비숍, R, r: 룩, Q, q: 퀸

chess = []
total_w, total_b = 0, 0

for _ in range(8):
    line = input()
    chess.append(line)

for i in range(8):
    for j in chess[i]:
        if (j.isupper()):
            if (j == 'K'):
                total_w += 0
            elif (j == 'P'):
                total_w += 1
            elif (j == 'N'):
                total_w += 3
            elif (j == 'B'):
                total_w += 3
            elif (j == 'R'):
                total_w += 5
            elif (j == 'Q'):
                total_w += 9

        else:
            if (j == 'k'):
                total_b += 0
            elif (j == 'p'):
                total_b += 1
            elif (j == 'n'):
                total_b += 3
            elif (j == 'b'):
                total_b += 3
            elif (j == 'r'):
                total_b += 5
            elif (j == 'q'):
                total_b += 9

total = total_w - total_b
print(total)