# 14501
# 퇴사하는 날 N, Ti(상담하는 데 걸리는 시간)와 Pi(가격)가 공백으로 구분되어 주어질 때
# 퇴사하기 전까지 최대로 얻을 수 있는 수익 출력하기
# 문제 이해 필요(2023.11.10) >> 답 불일치(2023.11.11, 12, 13)

n = int(input())
salary = []
count = n - 1; price = 0

for i in range(n):
    temp_list = list(map(int, input().split(' ')))
    salary.append(temp_list)

for i in range(n - 1, -1, -1):
    if (i > 0):
        if (i + 1 + salary[i][0] <= n):
            if (salary[i][0] <= salary[i + 1][0]):
                print(i)
                print(salary[i])
                price += salary[i][1]
    

print(price)

#----------------------------------------------------------------

n = int(input())
salary = []
count = n - 1; price = 0

for i in range(n):
    temp_list = list(map(int, input().split(' ')))
    salary.append(temp_list)

for i in range(n - 1, -1, -1):
    print(i, count)
    if (i + salary[i][0] + 1 <= n):
        if (salary[i][0] <= salary[i - 1][0]):
            print(salary[i])

            price += salary[i][1]
            count -= salary[i][0]

            print(i, count)

    else:
        count -= 1

print(price)