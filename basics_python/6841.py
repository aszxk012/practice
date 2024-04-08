# 6841
# 각 단어에 해당하는 뜻 출력
# 출력형식 오류 발생(2024.03.19, 20) > 수정 완료(2024.03.21)

dic = {"CU": "see you", ":-)": "I’m happy", ":-(": "I’m unhappy", ";-)": "wink",
       ":-P": "stick out my tongue", "(~.~)": "sleepy", "TA": "totally awesome",
       "CCC": "Canadian Computing Competition", "CUZ": "because", "TY": "thank-you",
       "YW": "you’re welcome", "TTYL": "talk to you later"}

while True:
    string = input()
        
    if (string in dic):
        print(dic[string])
    else:
        print(string)

    if (string == "TTYL"):
        break