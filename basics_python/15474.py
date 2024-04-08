# 15474
# 세트 X는 A개에 B엔, 세트 Y는 C개에 D엔일 때
# 연필 N개를 구매할 수 있는 최소 금액 출력하기
# 시간초과 추후 수정(23.12.11, 24.02.11)

n, a, b, c, d = map(int, input().split(' '))
price_a = 0
price_b = 0
count_a = 0
count_b = 0

while True:
    if (count_a == n):
        if (count_a == count_b):
            if (price_a >= price_b):
                print(price_b)
            else:
                print(price_a)

        else:
            print(price_a)

        break

    elif (count_b == n):
        if (count_a == count_b):
            if (price_a >= price_b):
                print(price_b)
            else:
                print(price_a)
        
        else:
            print(price_b)
        break

    else:
        price_a += b
        price_b += d

        count_a += a
        count_b += c

# ---------------------------------------------------

N, A, B, C, D = map(int, input().split())

Y_sets = N // C
remaining_pencils = N - Y_sets * C

total_price = min(Y_sets * D + remaining_pencils * B, (N // A + (1 if N % A != 0 else 0)) * B)

print(total_price)
