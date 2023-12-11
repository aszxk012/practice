# 28927
# 첫번째 줄은 Max가 본 트레일러, tv쇼, 영화 수
# 두번재 줄은 Mel이 본 트레일러, tv쇼, 영화 수
# 트레일러는 3분, tv쇼는 20분, 영화는 2시간 동안 진행될 때
# 누가 더 취미에 더 많은 시간을 보냈는지 출력하기
# 동일하다면 Draw 출력

max_t, max_tv, max_movie = map(int, input().split(' '))
mel_t, mel_tv, mel_movie = map(int, input().split(' '))

max_time = (3 * max_t) + (20 * max_tv) + (120 * max_movie)
mel_time = (3 * mel_t) + (20 * mel_tv) + (120 * mel_movie)

if max_time > mel_time:
    print("Max")
elif max_time < mel_time:
    print("Mel")
else:
    print("Draw")