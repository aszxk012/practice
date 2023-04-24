# 5063
# 입력받은 테스트 케이스 개수만큼 광고를 하지 않았을 때의 수익, 광고를 했을 때의 수익, 광고 비용을 입력받은 후
# 광고를 해야하면 "advertise", 별 차이가 없다면 "does not matter", 하지 말아야한다면 "do not advertise" 출력

test = int(input())
result = []

for _ in range(test):
    r, e, c = map(int, input().split(' '))

    if r > (e - c):
        result.append("do not advertise")
    elif r < (e - c):
        result.append("advertise")
    elif r == (e - c):
        result.append("does not matter")

for i in range(len(result)):
    print(result[i])