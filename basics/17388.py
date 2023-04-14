# 17388
# 숭실, 고려, 한양 순으로 참여도 입력
# 세 개의 합이 100이 넘으면 pass
# 100이 넘지 않으면 제일 참여도가 적은 대학 출력

def Compare(num1, num2, num3):
    univ = [num1, num2, num3]
    min_univ = min(univ)

    return min_univ

soongsil, korea, hanyang = map(int, input().split(' '))

if soongsil + korea + hanyang >= 100:
    print("OK")
else:
    min_univ = Compare(soongsil, korea, hanyang)

    if min_univ == soongsil:
        print("Soongsil")
    elif min_univ == korea:
        print("Korea")
    elif min_univ == hanyang:
        print("Hanyang")