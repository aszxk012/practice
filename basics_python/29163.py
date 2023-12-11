# 29163
# 짝수의 개수가 홀수의 개수보다 더 많을 때 Happy, 그렇지 않으면 Sad 출력하기

count_odd = 0 # 홀수
count_even = 0 # 짝수

n = int(input())

num = list(map(int, input().split(' ')))

if len(num) <= n:
    for i in num:
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

        
    if count_even > count_odd:
        print("Happy")
    else:
        print("Sad")