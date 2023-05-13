# 4562
# test case 입력받아 좀비가 먹는 뇌의 수와 좀비가 필요한 뇌의 수 비교하기

test = int(input())
result = []

for _ in range(test):
    eat_brain, need_brain = input().split(' ')
    eat_brain, need_brain = int(eat_brain), int(need_brain)

    if eat_brain >= need_brain:
        result.append("MMM BRAINS")

    else:
        result.append("NO BRAINS")

for i in range(len(result)):
    print(result[i])