# 1978
# n개의 숫자 중 소수가 몇 개인지 출력하기

test = int(input())
nums = list(map(int, input().split(' ')))
max_num = max(nums)

count = 0

if len(nums) == test:
    for i in nums:
        factors = []
        
        if i == 1:
            continue
        
        for j in range(1, i + 1):
            if i % j == 0:
                factors.append(j)
                
        factors = list(set(factors))
        
        if(len(factors) == 2):
            count += 1
            
print(count)