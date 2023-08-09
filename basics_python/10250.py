# 10250
# 테스트 케이스만큼 h, w, n을 입력받는다.
# h = 호텔 층 수
# w = 각 층의 방 수
# n = 몇 번째 손님인지
# 첫번째 손님은 101호, 두번째 손님은 201호에 배청하는 방식
# n번째 손님에게 배정되는 호텔의 방 번호 출력하기

test = int(input())

for i in range(test):
    h, w, n = map(int, input().split(' '))
    room = 1
    count = 1
    
    for i in range(n):
        room += 100
        
        if room > count + (100 * h):
            room -= (100 * h)
            room += 1
            count += 1
    
    print(room)