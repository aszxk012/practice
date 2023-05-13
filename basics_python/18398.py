# 18398
# 테스트 케이스 개수 입력 받은 후 테스트 케이스만큼의 문제 수 입력받기, 두 수 입력 받기
# 차례대로 두 수의 합, 두 수의 곱 출력하기

test = int(input())
sum = []
multi = []

for _ in range(test):
    problem = int(input())

    for _ in range(problem):
        a, b = map(int, input().split(' '))
        sum.append(a + b)
        multi.append(a * b)

for i in range(len(sum)):
    print(sum[i], multi[i])