# 4892
# n0를 생각하기
# n1 = 3 * n0 > 짝수, 홀수
# 짝수일때 n2 = n1/2, 홀수일떄 n2 = (n1 + 1)/2
# n3 = 3 * n2
# n4 = n3 / 9 (나눗셈의 몫)
# n1이 짝수일때, n0 = 2 * n4, 홀수일때 n0 = 2 * n4 + 1

result = []
num = []

while True:
    n0 = input()
    n0 = int(n0)

    if n0 == 0:
        break

    else:
        n1 = 3 * n0

        if n1 % 2 == 0:
            n2 = n1 / 2
        else:
            n2 = (n1 + 1) / 2

        n3 = 3 * n2
        n4 = n3 // 9

        if n1 % 2 == 0:
            n0 = 2 * n4
            num.append(int(n4))
            result.append("even")

        else:
            n0 = 2 * n4 + 1
            num.append(int(n4))
            result.append("odd")

for i in range(len(result)):
    print(str(i + 1) + ".", result[i], num[i])