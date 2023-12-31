# 20976
# a, b, c가 주어질 때 두 번째로 큰 숫자 출력하기

list_num = list(map(int, input().split(' ')))
max_num = max(list_num)

if (max_num == list_num[0]):
    if (list_num[1] > list_num[2]):
        print(list_num[1])
    else:
        print(list_num[2])

elif (max_num == list_num[1]):
    if (list_num[0] > list_num[2]):
        print(list_num[0])
    else:
        print(list_num[2])

else:
    if (list_num[0] > list_num[1]):
        print(list_num[0])
    else:
        print(list_num[1])