# 21612
# 끓는점 구하기

temperature = int(input())
p = 5 * temperature - 400
result = 0

if temperature < p:
    result = -1
elif temperature == p:
    result = 0
else:
    result = 1

print(p)
print(result)