# 5554
# 첫번째 줄은 집에서 학교까지의 이동시간
# 두번째 줄은 학교에셔 PC방까지의 이동시간
# 세번째 줄은 PC방에서 학원까지의 이동시긴
# 마지막 줄은 학원에서 집까지의 이동시간
# 총 x분 y초의 이동시간 출력, x는 첫째줄에, y는 두번째 줄에 출력
# 추후 수정(2023.07.22) > 수정할 사항 없음(2023.07.23)

times = []
sum = 0

for i in range(4):
    time = int(input())
    times.append(time)
    
    sum += times[i]

print(sum // 60)
print(sum % 60)
