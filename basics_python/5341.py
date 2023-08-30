# 5341
# n층엔 1개의 블록, n-1층엔 2개의 블록, ... , 1층엔 n개의 블록을 사용하여 피라미드를 만든다
# 피라미드 n층을 쌓기 위해 필요한 블록의 수 출력하기

while True:
    n = int(input())
    sum = 0
    
    if n == 0:
        break
    
    for i in range(1, n + 1):
        sum += i
        
    print(sum)