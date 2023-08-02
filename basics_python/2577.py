# 2577
# 세 자연수 a, b, c가 주어질 때, a x b x c의 결과에서
# 0부터 9까지 숫자가 몇 번 쓰였는지 출력하기

a = int(input())
b = int(input())
c = int(input())

cal = str(a * b * c)
result = []

for _ in range(10):
    result.append(0)

for i in cal:
    for j in range(10):
        if int(i) == j:
            result[j] += 1
    
for i in range(10):
    print(result[i])