# 14501
# 퇴사하는 날 N, Ti(상담하는 데 걸리는 시간)와 Pi(가격)가 공백으로 구분되어 주어질 때
# 퇴사하기 전까지 최대로 얻을 수 있는 수익 출력하기
# 문제 이해 필요(2023.11.10)

n = int(input())
salary = []

for i in range(n):
    temp_list = list(map(int, input().split(' ')))
    salary.append(temp_list)

for i in range(n - 1, -1, -1):
    print(salary[i][0])
    #if (n + salary[i][0] <= n + 1):
     #   print(salary[i])