# 27294
# 시간과 술 유무를 숫자로 입력받아 초밥의 밥알 개수 구하기
# 11시 이하면 아침, 12 ~ 16 점심, 17 ~ 저녁, 술o 1, 술x 0
# 술하고 같이 먹거나 점심 식사가 아니면 초밥의 밥알은 280개, 점심식사면서 술과 같이 먹지 않을 때는 초밥의 밥알은 320개

time, drink = map(int, input().split(' '))
sushi = 0

if (12 <= time <= 16) and (drink == 0):
    sushi = 320
elif (drink == 1) or not(12 <= time <= 16):
    sushi = 280

print(sushi)