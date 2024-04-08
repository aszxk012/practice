# 26736
# A와 B로 이루어진 문자열이 주어진다.
# A의 개수와 B의 개수를 출력 형식(N : M)에 맞춰 출력

string = input()
a, b = 0, 0

for i in string:
    if (i == "A"):
        a += 1
    elif (i == "B"):
        b += 1

print("%d : %d" % (a, b))