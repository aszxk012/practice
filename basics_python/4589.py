# 4589
# 서로 다른 양의 정수가 순서대로 정렬되어 있는지 출력
# 내림차순으로 정렬했을 경우 "Ordered" 출력 불가(2024.04.20.) > 해결(2024.04.21.)

n = int(input())
result = []

for _ in range(n):
    num = list(map(int, input().split(' ')))
    num_sort = sorted(num)
    num_sort_r = sorted(num, reverse=True)

    if ((num == num_sort) or (num == num_sort_r)):
        result.append("Ordered")
    else:
        result.append("Unordered")

print("Gnomes:")
for i in range(n):
    print(result[i])