# 8437
# 총 사과 개수와 A가 더 가지고 잇는 사과가 몇 개인지 입력받아
# A와 B가 갖고 있는 사과 개수 출력하기

apple = int(input())
dif = int(input())

a, b = 0, 0
apple_dif = apple - dif

a = apple_dif // 2
b = a + dif

print(b)
print(a)