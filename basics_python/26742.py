# 26742
# 양말 색상을 나타내는 B와 C로 구성된 문자열이 입력된다.
# B는 흰색, C는 검은색 양말은 나타낸다.
# 입력에서 설명된 양말들에서 만들 수 있는 단색 양말 쌍의 수 출력

string = input()
b, c = 0, 0

for i in range(len(string)):
    if (string[i] == "B"):
        b += 1
    elif (string[i] == "C"):
        c += 1

result_b = b // 2
result_c = c // 2

result = result_b + result_c

print(result)