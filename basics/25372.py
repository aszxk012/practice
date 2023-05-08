# 25372
# 비밀번호는 6자리 이상 9자리 이하
# 문져아려을 입력받아 사용할 수 있는 비밀번호인지 판단하기

test = int(input())
result = []

for _ in range(test):
    string = input()

    if 6 <= len(string) <= 9:
        result.append("yes")
    else:
        result.append("no")

for i in range(len(result)):
    print(result[i])