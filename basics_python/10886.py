# 10886
# 설문조사

test = int(input())
count_1 = 0
count_0 = 0

for _ in range(test):
    answer = input()

    if answer == '1':
        count_1 += 1

    elif answer == '0':
        count_0 += 1

if count_0 < count_1:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")