test = int(input())
sum = 0

for i in range(test):
    std, apple = map(int, input().split())
    
    temp = apple % std
    sum += temp
    
print(sum)