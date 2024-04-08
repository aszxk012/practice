# 30501
# 관우를 죽인 범인의 이름에는 S가 들어갈 때
# 관우를 죽인 용의자 이름의 리스트에서 범인의 이름 출력

n = int(input())

for _ in range(n):
    name = input()

    if ("S" in name):
        print(name)