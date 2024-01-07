# 23795
# 양의 정수가 입력되고 마지막 줄에 끝을 의미하는 -1이 입력된다.
# 입력된 수의 합 출력

sum = 0
while True:
    n = int(input())

    if (n == -1):
        print(sum)
        break
    
    else:
        sum += n