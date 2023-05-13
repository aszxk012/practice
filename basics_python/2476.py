# 2476
# 게임에 참여할 사람의 수만큼 주사위 세 개의 눈을 입력받는다.
# 같은 눈 세 개 10,000 + 같은눈 x 1,000
# 같은 눈 두 개 1,000 + 같은 눈 x 100
# 다 다른 눈 그중 가장 큰 눈 x 100
# 게임에 참여한 사람들의 상금 중 가장 큰 상금 출력

people = int(input())
max_prize = 0

for _ in range(people):
    dice1, dice2, dice3 = map(int, input().split(' '))

    if dice1 == dice2 and dice2 == dice3:
        cur_prize = 10000 + dice1 * 1000
    elif dice1 == dice2 or dice1 == dice3:
        cur_prize = 1000 + dice1 * 100
    elif dice2 == dice3:
        cur_prize = 1000 + dice2 * 100
    else:
        max_dice = max(dice1, dice2, dice3)
        cur_prize = max_dice * 100

    max_prize = max(max_prize, cur_prize)


print(max_prize)