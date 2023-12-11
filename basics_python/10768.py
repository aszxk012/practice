# 10768
# 월과 일을 입력받아 2월 18일 전이면 Before, 후면 After,
# 18일이면 Special 출력하기

m = int(input())
d = int(input())

if (m > 2):
    print("After")
elif (m < 2):
    print("Before")
else:
    if (d == 18):
        print("Special")
    elif (d > 18):
        print("After")
    else:
        print("Before")