# 20833
# 한 변의 길이가 1인 작은 정육면체를 붙여 더 큰 정육면체를 만든다.
# 한 번에 길이가 각각 1부터 n인 정육면체를 만든다고 할 떄
# 몇 개의 작은 정육면체가 필요한지 출력

n = int(input())
result = 0

for i in range(1, n + 1):
    result += i * i * i

print(result)