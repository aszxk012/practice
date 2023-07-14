# 9295
# 테스트 케이스만큼 주사위를 두 번 던져 나온 두 수가 주어진다.
# 두 수의 합을 테스트 케이스 번호와 함께 출력한다.

test = int(input())
result = []

for _ in range(test):
    x, y = map(int, input().split())
    result.append(x + y)
    
for i in range(test):
    print("Case", i + 1, end='') 
    print(":", result[i])