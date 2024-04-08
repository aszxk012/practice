# 26332
# 상점에서 하나만 사면 할인이 안되며, 하나 이상 구매시 추가 품목 당 2달러씩 할인이 된다.
# 고객이 구매한 품목의 수와 한 품목의 가격을 고려하여 고객의 총 비용 계산
# 고객이 구매한 품목의 수와, 하나의 품목에 대한 가격이 주어질 때
# 첫 번째 줄에는 두 입력 값을 공백으로 구분하여 출력, 두 번째 줄에는 총 비용 출력

n = int(input())

for i in range(n):
    c, p = map(int, input().split(' '))
    total = 0

    if (c < 2):
        total = c * p

    else:
        cur = c - 1
        
        total = (c * p) - (cur * 2)

    print(c, p)
    print(total)