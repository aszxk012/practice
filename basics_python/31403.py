# 31403
# A, B, C가 각각 주어질 때 수와 문자열로 생각할 경우 A + B - C 출력
# 에러 발생(2024.04.22.) > 문제 해결(2024.04.23.)

a = input()
b = input()
c = input()

an = int(a)
bn = int(b)
cn = int(c)

total_n = an + bn  - cn
total = a + b
total, c = int(total), int(c)
total -= c

print(total_n)
print(total)