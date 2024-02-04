# 21665
# m X n 흑백 사진 원본과 흑백 반전한 사진이 입력된다.
# 잘못 반전된 픽셀의 개수 출력
# 원본과 반전 픽셀 간의 공백 해결 불가(2024.01.17) > 해결(2024.01.18)

m, n = map(int, input().split(' '))
count = 0
result = []

for i in range(m + 1):
    input_pic = input()

    result_input = ''
    if (len(input_pic) != 0):
        for j in range(len(input_pic)):
            if (input_pic[j] == "B"):
                result_input += "W"
            elif (input_pic[j] == "W"):
                result_input += "B"
        result.append(result_input)

for i in range(m):
    after_pic = input()
    for j in range(len(after_pic)):
        if (result[i][j] != after_pic[j]):
            count += 1

print(count)