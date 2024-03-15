# 31450
# M개의 메달을 K명의 아이들에게 똑같이 나눠줄 수 있으면 "Yes"를, 아니면 "No" 출력

m, k = map(int, input().split(' '))

if (m % k == 0):
    print("Yes")
else:
    print("No")