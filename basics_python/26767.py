# 26767
# 참가자들이 돌아가며 n까지 외친다.
# 7의 배수이면서 11의 배수는 아니라면 Huura!를 외친다.
# 7의 배수가 아니면서 11의 배수라면 Super!를 외친다.
# 7의 배수이면서 11의 배수라면 Wiwat!을 외친다.

n = int(input())

for i in range(1, n + 1):
    if ((i % 7 == 0) and (i % 11 != 0)):
        print("Hurra!")
    elif ((i % 7 != 0) and (i % 11 == 0)):
        print("Super!")
    elif ((i % 7 == 0) and (i % 11 == 0)):
        print("Wiwat!")
    else:
        print(i)