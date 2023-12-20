# 18691
# 1, 2, 3그룹은 각각 사탕 1개를 획득하기 위해 1, 3, 5 킬로미터를 걸어야한다.
# 그룹, 처음 가지고 있던 사탕 개수, 진화에 필요한 사탕 개수가 주어질 때
# 몇 걸음 걸어야 필요한 사탕의 개수를 다 채울 수 있는지 출력

num = int(input())

for _ in range(num):
    g, c, e = map(int, input().split(' '))
    kilo = 0
    need = 0
    
    if c >= e:
        need = 0
    
    else:
        if g == 1:
            kilo = 1
            need = (e - c) * kilo

        elif g == 2:
            kilo = 3
            need = (e - c) * kilo

        elif g == 3:
            kilo = 5
            need = (e - c) * kilo

    print(need)