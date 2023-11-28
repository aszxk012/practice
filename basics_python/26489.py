# 26489
# 몇 번 입력받았는지 출력하기
# EOF 처리

count = 0

while True:
    try:
        string = input()
        count += 1

    except EOFError:
        print(count)
        break