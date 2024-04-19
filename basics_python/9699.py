# 9699
# 쌀 몇 포대를 다섯 고아원으로 보내려한다. 가장 무거운 포대는 알-아민 고아원으로 보낸다.
# 가장 가벼운 포대는 무티아라 고아원으로 보낸다. 어떤 포대가 알-아민 고아원으로 가는지 계산
# 각 테스트 케이스에 대해 "Case #x: 정수" 형태로 출력, x는 1부터 시작

n = int(input())

for i in range(1, n + 1):
    weight = list(map(int, input().split(' ')))
    max_w = max(weight)

    print("Case #%d: %d" % (i, max_w))