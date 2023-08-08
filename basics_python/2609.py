# 2609
# 두 자연수 입력받아 최대 공약수, 최소 공배수 구하기

a, b = map(int, input().split(' '))
a_divisor = []
b_divisor = []
divisor, multiple = 1, 1

if a > b:
    a, b = b, a

for i in range(1, b + 1):
    if (a % i == 0):
        a_divisor.append(i)
        
    if (b % i == 0):
        b_divisor.append(i)
        
    if (a % i == 0) and (b % i == 0):
        divisor = i
        

a_factor = a // divisor
b_factor = b // divisor
multiple = divisor * a_factor * b_factor

print(divisor)
print(multiple)
