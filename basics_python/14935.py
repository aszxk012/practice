# 14935
# f(x)는 입력으로 주어진 첫 자리 수와 x의 자리수를 곱한 결과를 반환하는 함수
# f(x)의 결과를 다시 f(x)의 입력으로 넣고 동일한 수가 나올때,
# 입력 x를 FA 수라고 한다. 입력 x가 FA수인지 아닌지 판별 후 출력하기
# 함수 에러 >> 추후 수정(2023.11.27), 에러 수정, 답 안나옴.. (2023.11.28)

def fx(x):
    x_str = str(x)
    x_1 = int(x_str[0])
    x_len = len(x_str)

    return x_1 * x_len

def is_fa_number(x):
    result = []
    i = 0

    while True:
        answer = fx(x)
        x = answer
        result.append(answer)
        
        if i >= 2 and result[i] == result[i - 1] == result[i - 2]:
            return True  # FA 수인 경우
        elif i >= 100:  # 임의의 횟수 (반복이 너무 길어지는 것을 방지하기 위해)
            return False  # FA 수가 아닌 경우

        i += 1

# 사용자로부터 입력 받기
user_input = input()

# FA 수 여부 확인
if is_fa_number(int(user_input)):
    print("FA")
