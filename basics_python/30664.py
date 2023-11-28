# 30664
# 식별번호가 42의 배수인 카드 찾기
# 0이 입력될 경우 종료
# 42의 배수인경우 PREMIADO, 아니면 TENTE NOVAMENTE 출력하기

while True:
    n = int(input())
    if n == 0:
        break;
    
    if (n % 42 == 0):
        print("PREMIADO")
    else:
        print("TENTE NOVAMENTE")