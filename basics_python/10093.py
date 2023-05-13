# 10093
# 두 정수 사이에 있는 정수의 개수와
# 두 수 사이에 있는 수를 오름차순으로 정렬한다.

def Sort(num1, num2):
    if num1 > num2:
        big = num1
        small = num2
    else:
        big = num2
        small = num1

    num_count = big - small - 1
    num_list = ''

    if num_count < 0:
        num_count = 0

    for i in range(num_count):
        num_list += str(small + i + 1)
        
        if (small + i + 1) == big:
            pass
        else:
            num_list += ' '

    return num_count, num_list

a, b = map(int, input().split(' '))
num_count, num_list = Sort(a, b)

print(num_count)
print(num_list)