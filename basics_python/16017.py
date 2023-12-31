# 16017
# 스팸 전화의 전화번호 마지막 네 자리 규칙은 다음과 같다
# 첫 번째 자리와 마지막 자리가 8 또는 9
# 두 번째와 세 번째 자리는 같다.
# 스팸번호인지 아닌지 출력하기

num_list = []

for _ in range(4):
    num = int(input())
    num_list.append(num)

if ((num_list[0] == 8) or (num_list[0] == 9)):
    if ((num_list[-1] == 8) or (num_list[-1] == 9)):
        if (num_list[1] == num_list[2]):
            print("ignore")
        
        else:
            print("answer")
    else:
        print("answer")
else:
    print("answer")