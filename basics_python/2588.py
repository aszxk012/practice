# 2588
# 세 자리 자연수 두 개가 주어질 때 곱셈하는 과정을 구하는 프로그램

num1 = input()
num2 = input()

# num2의 100의 자리, 10의 자리, 1의 자리 수
num2_100, num2_10, num2_1 = num2[0], num2[1], num2[2]
num1, num2, num2_100, num2_10, num2_1 = int(num1), int(num2), int(num2_100), int(num2_10), int(num2_1)

print(num1 * num2_1)
print(num1 * num2_10)
print(num1 * num2_100)
print(num1 * num2)