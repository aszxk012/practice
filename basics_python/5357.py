# 5357
# 입력받은 문자열의 중복을 제거하여 출력하기
# 예제 ABBBBAACC에 대해서 ABAC가 나오지 않음, 추후 수정(2023.10.28)
# 수정 완료(2023.10.29)

num = int(input())

for i in range(num):
    string = input()
    result = string[0]

    for j in range(1, len(string)):
        if string[j] != result[-1]:
            result += string[j]

    print(result)

