# 25628
# 햄버거 빵이 A개, 햄버거 패티가 B개 있는데, 이 빵과 패티를 가지고 최대한 햄버거를 만든다.
# 한 햄버거를 만드는 데에 빵 2개, 패티 1개가 사용된다.
# 남는 빵이나 패티가 있어도 된다고 할 때, 만들 수 있는 최대 개수 출력

a, b = map(int, input().split(' '))
total = 0

while True:
    if ((a > 1) and (b > 0)):
        a -= 2
        b -= 1
        total += 1

    else:
        break

print(total)