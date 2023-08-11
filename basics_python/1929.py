# 1929
# m 이상 n 이하의 소수 모두 출력
# 시간초과 추후 수정(2023.08.11)

m, n = map(int, input().split(' '))
result = []

for i in range(m, n + 1):
    factors = []
    
    for j in range(1, i + 1):
        if i % j == 0:
            factors.append(j)
            
    factors = list(set(factors))
    
    if(len(factors) == 2):
        result.append(i)
            
for num in result:
    print(num)