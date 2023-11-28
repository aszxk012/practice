# 11365
# 주어진 문장을 뒤집어서 출력하기
# END가 주어진다면 종료(해독하지 않음)

while (True):
    string = input()
    
    if string == 'END' or string == 'end':
        break
    
    print(string[::-1])