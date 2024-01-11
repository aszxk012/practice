# 21354
# 누가 더 돈을 많이 벌었는지 출력
# 사과의 가격은 7, 배의 가격은 13일 때, 
# Axel이 판 사과의 수와 Petra가 판 배의 수가 순서대로 주어진다.
# 둘이 같은 금액을 팔았다면 lika 출력

apple, pear = map(int, input().split(' '))
apple *= 7
pear *= 13

if (apple > pear):
    print("Axel")
elif (apple < pear):
    print("Petra")
else:
    print("lika")