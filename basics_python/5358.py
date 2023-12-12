# 5358
# i를 e로, e를 i로, I를 E로, E를 I로 바꿔서 출력하기

while True:
    try:
        strings = input()
        result = ''
        for i in range(len(strings)):
            if strings[i] == 'i':
                result += 'e'

            elif strings[i] == 'I':
                result += 'E'

            elif strings[i] == 'e':
                result += 'i'
            
            elif strings[i] == 'E':
                result += 'I'

            else:
                result += strings[i]
                
        print(result)

    except EOFError:
        break