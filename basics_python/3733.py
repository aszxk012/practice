# 3733
# N명의 사람과 심사위원이 S개의 주식을 똑같이 분배함.(모두 분배할 필요X)
# x는 정수이며, 각 사람이 받는 주식의 수
# x의 최댓값 계산하여 출력하기
# EOF로 종료

while True:
    try:
        n, s = map(int, input().split(' '))
        n += 1
        x = s // n
        print(x)

    except EOFError:
        break