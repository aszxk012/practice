# 4101
# 두 양수가 주어졌을 때 첫 번째 수가 두 번째 수보다 큰지 구하는 프로그램

result = []

while True:
    nums = input()
    num1, num2 = nums.split(' ')
    num1, num2 = int(num1), int(num2)

    if nums == '0 0':
        break
        
    if num1 > num2:
        result.append("Yes")

    elif num1 <= num2:
        result.append("No")


for i in range(len(result)):
    print(result[i])