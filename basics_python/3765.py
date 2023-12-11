# 3765
# 입력 받은 그대로 출력하기
# EOF 처리

while True:
    try:
        string = input()
        print(string)

    except EOFError:
        break