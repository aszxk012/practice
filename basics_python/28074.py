# 28074
# 문자열이 주어질 떄, 주어진 문자열에 포함된 문자드을 이용하여
# "MOBIS"를 만들 수 있으면 "YES", 없으면 "NO" 출력

string = input()
string_list = list(string)
mobis = "MOBIS"

flag = True
for i in range(5):
    if (mobis[i] in string):
        pass
    else:
        flag = False

if (flag == True):
    print("YES")
else:
    print("NO")