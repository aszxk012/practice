# 28290
# 8개의 문자로 구성된 문자열이 입력된다.
# 해당 문자열을 보고 타법 출력

step = ["fdsajkl;", "jkl;fdsa", "asdf;lkj", ";lkjasdf",
        "asdfjkl;", ";lkjfdsa"]

string = input()

if (string == step[0]):
    print("in-out")
elif (string == step[1]):
    print("in-out")
elif (string == step[2]):
    print("out-in")
elif (string == step[3]):
    print("out-in")
elif (string == step[4]):
    print("stairs")
elif (string == step[5]):
    print("reverse")
else:
    print("molu")