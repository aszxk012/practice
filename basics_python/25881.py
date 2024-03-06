# 25881
# 처음 1000KWH 사용량에 대한 요율(KWH 당), 추가 사용량에 대한 요율(KWH 당),
# 고객의 에너지 소비량이 주어질 때 요금 출력

rate = list(map(int, input().split(' ')))
n = int(input())

for i in range(n):
    use = int(input())
    total = 0
    
    if (use <= 1000):
        total += use * rate[0]
    
    else:
        total += 1000 * rate[0]
        cur = use - 1000

        if (len(rate) >= 3):
            k = 1
            for j in range(1001, cur + 1, 1000):
                total += j * rate[k]
                k += 1
        else:
            total += cur * rate[1]

    print(use, total)