# 21300
# 맥주, 맥아, 와인, 탄산음료, 탄산수, 물 순으로 공병의 개수를 입력받아
# 환급액 계산하기
# 모두 5센트

bottles = input().split(' ')
sum = 0

for i in bottles:
    i = int(i)
    sum += i * 5
    
print(sum)