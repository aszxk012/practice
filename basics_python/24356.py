# 24356
# t1시 m1분부터 t2시 m2분까지 산책하며 호수를 한 바퀴 도는데에는 30분이 걸린다.
# 산책에 걸린 시간 m분과 호수를 오나전히 한바퀴 돈 횟수 n번 출력
# 산책시간이 23시간 ~ 24시간인 경우 오답(2024.02.16, 17, 18)

t1, m1, t2, m2= map(int, input().split(' '))

if (t1 > t2):
    if (m1 > m2):
        t2 += 23
        m2 += 60
    elif (m1 < m2):
        t2 += 24
        
elif (t1 == t2):
    if (m1 > m2):
        t2 += 23
        m2 += 60

diff_t = t2 - t1
diff_m = m2 - m1

m = diff_t * 60 + diff_m
n = m // 30

print(m, n)