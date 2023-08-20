# 2775
# a층의 b호에 살려면 a - 1층의 1호부터 b호까지 사람들의 수의 합만큼
# 사람을 데려와서 살아야한다.
# k층 n호에 몇명이 살고 있는지 출력하기
# 0층, 1호부터 있으며 0층의 i호에는 i명이 살고 있다.
# 원리 미숙지(2023.08.10)

def get_room(n):
    room = 1
    if n == 2:
        pass

    else:
        n -= 1
        get_room(n)
        
    return room
    
test = int(input())
floor_0 = []
floor_1 = []
sum = 0
room = 1

for i in range(1, 15):
    sum += i
    floor_0.append(i)
    floor_1.append(sum)

for _ in range(test):
    k = int(input())
    n = int(input())
    
    for i in range(2, k + 1):
        for j in range(2, n + 1):
            pass