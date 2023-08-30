# 27219
# 1일이 지날 때마다 I, 5일은 V로 표기
# 숫자 n이 주어질 때 어떤 표시가 있는지 출력하기

n = int(input())
string = ""

for i in range(1, n + 1):
    string += "I"
    
    if i % 5 == 0:
        if "V" in string:
            string = string.replace("IIIII", "", 1)
            string += "V"
        else:
            string = "V"

print(string)