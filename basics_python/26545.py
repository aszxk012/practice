# 26545
# n개의 정수를 입력받아 모두 더해서 출력하기

n = int(input())
sum = 0

for _ in range(n):
    a = int(input())
    
    sum += a
    
print(sum)