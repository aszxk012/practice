# 25591
# 인도식 곱셈 과정 및 결과 출력
# ex) 97 * 96
# a = 100 - 97, b = 100 - 96
# c = 100 - (a + b) -> 결과 값의 앞의 두 자릿수
# d = a * b -> 결과 괎의 뒤의 두 자릿수
# d를 100으로 나눈 몫과 나머지 = q, r
# a, b, c, d, q, r 을 첫 번째 줄에 출력
# 두 번째 줄에 곱셈 결과의 앞의 두 자릿수와 뒤의 두 자릿수 출력

n1, n2 = map(int, input().split(' '))
a = 100 - n1
b = 100 - n2
c = 100 - (a + b)
d = a * b
q = d // 100
r = d % 100
result = n1 * n2
result = str(result)

if (len(result) % 2 != 0):
    temp = result
    result = "0"
    result += temp

print(a, b, c, d, q, r)
print(int(result[:2]), int(result[2:]))