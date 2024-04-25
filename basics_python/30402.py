# 30402
# 주어진 사진이 어떤 고양이 사진인지 구분하기
# 흰색(w) = 춘배, 검은색(b) = 나비, 회색(g) = 영철
# 사진은 고양이(w, b, g) 또는 배경(r, o, y, p)으로 이루어져 있으며
# 한 사진에는 한마리의 고양이만 나온다.

pixel = []

for i in range(15):
    string = list(map(str, input().split(' ')))
    pixel.append(string)

cat = 0

for i in range(15):
    for j in range(15):
        if (pixel[i][j] == "w"):
            cat = 1
        elif (pixel[i][j] == "b"):
            cat = 2
        elif (pixel[i][j] == "g"):
            cat = 3

if (cat == 1):
    print("chunbae")
elif (cat == 2):
    print("nabi")
elif (cat == 3):
    print("yeongcheol")