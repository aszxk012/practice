# 25932
# 첫 번째 입력 라인은 데이터 셋을 확인할 수 있는 양의 정수 n이다.
# n개의 입력 라인에는 각 하나의 세트가 있으며 각 세트는 10개의 서로 다른 정수이다.
# 세트의 숫자는 선수들의 저지 번호를 나타낸다.
# Mack이 18번 저지를 입고 Zack이 17번 저지를 입는다고 가정할 때
# 쌍둥이 중 몇 명이 있는지를 나타내는 네 가지 메시지(mack, zack, both, none) 중 하나 출력
# 출력 후 한 줄 띄우기
# 둘 다 있는 both 출력 불가능(2024.04.15)

n = int(input())
zack, mack = 17, 18

for _ in range(n):
    string = input()
    players = list(map(int, string.split(' ')))
    
    print(string)
    
    if (zack in players):
        print("zack")
    
    elif (mack in players):
        print("mack")
    
    elif ((zack in players) and (mack in players)):
        print("both")
    
    else:
        print("none")

    print()