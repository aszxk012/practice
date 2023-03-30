# 25314
# 숫자를 입력받아 정수 자료형의 이름 구하기
# long int = 4 byte, long long int = 8 byte ...

num = int(input())
count = num // 4
count_str =  "long "

if num % 4 == 0:
    print(count_str * count + "int")

elif num % 4 != 0:
    print(count_str * (count + 1) + "int")