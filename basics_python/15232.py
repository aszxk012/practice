# 15232
# R과 C가 주어질 때, R개의 줄에 C개의 별(*)을 출력한다.

r = int(input())
c = int(input())

for i in range(r):
    string = ''
    for j in range(c):
        string += "*"
    print(string)