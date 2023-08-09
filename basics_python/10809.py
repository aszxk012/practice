# 10809
# 문자열이 주어질 때, 각각의 알파벳이 단어에 포함되어 있는 경우
# 처음에 등장하는 위치를, 포함되어 있지 않은 경우에는 -1 출력하기

string = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = []

for i in alphabet:
    if i in string:
        index_num = string.index(i)
        result.append(index_num)
    else:
        result.append(-1)

for i in result:
    print(i, end = ' ')