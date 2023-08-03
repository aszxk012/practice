# 2920
# 1부터 8까지 입력받아 오름차순이면 ascending, 내림차순이면 descending,
# 둘 다 아니라면 mixed 출력하기

record = input().split(' ')
sort_asc = []
sort_desc = []

for i in range(len(record)):
    record[i] = int(record[i])
    sort_asc.append(i + 1)
    sort_desc.append((len(record) - i))

if record == sort_asc:
    print("ascending")
elif record == sort_desc:
    print("descending")
else:
    print("mixed")