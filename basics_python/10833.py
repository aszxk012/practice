# 10833
# 학교의 학생 수와 사과의 개수가 주어졌을 때, 학생들에게 나눠주고 남은
# 사과의 총 개수 구하기

test = int(input())
sum = 0

for i in range(test):
    std, apple = map(int, input().split())
    
    temp = apple % std
    sum += temp
    
print(sum)