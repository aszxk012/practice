# 28235
# 구호 SONGDO는 HIGHSCHOOL로, 구호 CODE는 MASTER로, 구호 2023은 0611로, 구호 ALGORITHM은 CONTEST로 응원

cheer = {"SONGDO": "HIGHSCHOOL", "CODE": "MASTER", "2023": "0611", "ALGORITHM": "CONTEST"}

string = input()

for k in cheer:
    if string == k:
        print(cheer[k])