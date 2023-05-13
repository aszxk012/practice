# 5596
# 민국이와 만세의 4과목 총점 중 큰 점수 출력하기
# 동일할 땐 민국이 총점 출력

s = input().split(' ')
t = input().split(' ')

total_s = 0
total_t = 0

for i in range(len(s)):
    total_s += int(s[i])
    total_t += int(t[i])


if total_s >= total_t:
    print(total_s)
else:
    print(total_t)