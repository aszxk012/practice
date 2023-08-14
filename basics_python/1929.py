# 1929
# m 이상 n 이하의 소수 모두 출력
# 시간초과 추후 수정(2023.08.11) > 

m, n = map(int, input().split(' '))
result = []

for i in range(m, n + 1):
    factors = []
    
    for j in range(1, i + 1):
        if i % j == 0:
            factors.append(j)
            
    factors = list(set(factors))
    
    if(len(factors) == 2):
        print(i)



# ==========================================================
# 에라토스테네스의 체 사용하여 풀기
# 런타임 에러 추후 수정(2023.08.14)

m, n = map(int, input().split(' '))
prime_list = [True] * [n + 1]
prime_list[0], prime_list[1] = False, False

for i in range(2, int(n ** 0.5) + 1):
    if prime_list[i]:
        for j in range(i * 2, n + 2, i):
            prime_list[j] = False

for i in range(m, n + 1):
    if prime_list[i]:
        print(i)