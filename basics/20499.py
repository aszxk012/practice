# 20499
# k, d, a를 입력받아 k + a < d 이거나 d = 0이면 hasu, 그렇지 않으면 gosu 출력

k, d, a = map(int, input().split('/'))

if k + a < d:
    print("hasu")
elif d == 0:
    print("hasu")
else:
    print("gosu")