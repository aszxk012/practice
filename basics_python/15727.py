# 15727
# 1분에 1에서 5까지 거리를 갈 수 있을 때, 주어진 거리는 몇 분이 걸리는지 출력하기

length = int(input())
min = 0

while length > 5:
    length -= 5
    min += 1
    
    if (length <= 5):
        break
    
print(min + 1)