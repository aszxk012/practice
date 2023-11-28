# 14935
# f(x)는 입력으로 주어진 첫 자리 수와 x의 자리수를 곱한 결과를 반환하는 함수
# f(x)의 결과를 다시 f(x)의 입력으로 넣고 동일한 수가 나올때,
# 입력 x를 FA 수라고 한다. 입력 x가 FA수인지 아닌지 판별 후 출력하기
# 함수 에러 >> 추후 수정(2023.11.27), 에러 수정, 답 안나옴.. (2023.11.28)

def fx(x):
    x_1 = int(str(x)[0])
    x_len = len(str(x))

    return x_1 * x_len

x = input()
result = []
i = 0

while True:
    answer = fx(x)
    x = answer
    result.append(answer)
    
    if i == 0:
        continue
    
    elif ((result[i] == result[i - 1]) and (result[i] == result[i - 2])):
        print("FA")
        break

    i += 1
