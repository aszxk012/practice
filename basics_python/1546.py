# 1546
# 모든 점수를 (점수 / 점수 최댓값) * 100으로 바꾼 후 평균 구하기

test_num = int(input())
test = list(map(int, input().split(' ')))
new_test = []
max_score = 0
total = 0

for i in range(len(test)):
    if max_score >= test[i]:
        pass
    else:
        max_score = test[i]

for j in range(len(test)):
    new_score = (test[j] / max_score) * 100

    new_test.append(new_score)

for k in range(len(new_test)):
    total += new_test[k]

avg = total / (len(new_test))
print(avg)