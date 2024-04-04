# 31261
# 숫자를 하나 생각한다.
# 그 수를 a로 나누고 결과에서 a를 뺀 다음
# 결과 숫자로 다시 동일한 작업을 수행하면 b가 나온다.
# 원래 숫자를 구한다

a, b = map(int, input().split(' '))

result = (((b + a) * a) + a ) * a

print(result)