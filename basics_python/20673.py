# 20673
# 신규 확진 수의 평균과 하루 신규 입원 수의 평균이 주어질 때
# 확진자 수가 50 이하, 입원 수가 10 이하라면 White, 입원수가 30 이상이라면 Red, 그 외는 Yellow로 출력

a = int(input())
b = int(input())

if ((a <= 50) and (b <= 10)):
    print("White")
elif (b > 30):
    print("Red")
else:
    print("Yellow")