# 14652
# 세로가 N, 가로가 M인 관중석에서 관중석 번호 K의 좌표 출력하기
# 시간 초과
n, m, k = map(int, input().split(' '))
a, b = 0, 0

for i in range(k):
    b += 1
    
    if b == m:
        a += 1
        b = 0
        
print(a, b)


# 시간 초과 수정 코드
n, m, k = map(int, input().split(' '))
a = k // m
b = k % m

print(a, b)