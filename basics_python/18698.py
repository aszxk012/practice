# 18698
# U는 손을 들어올린 상태로 걷는 상태를, D는 넘어진 상태를 의미한다
# 넘어지기 전까지 몇 걸음을 걸었는지 출력하기

num = int(input())

for i in range(num):
    count = 0
    steps = input()

    for j in range(len(steps)):
        if ("D" in steps):
            if (steps[j] == "U"):
                count += 1
        
            elif (steps[j] == "D"):
                print(count)
                break
        
        else:
            print(len(steps))
            break