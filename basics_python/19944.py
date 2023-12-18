# 19944
# 뉴비는 1, 2학년, 올드비는 N학년 이하면서 뉴비가 아닌 학생,
# TLE는 뉴비도 올드비도 아닌 학생으로 정의했을 때
# N과 M이 주어지고 M학년은 뉴비인지 올드비인지 TLE인지 출력하기

n, m = map(int, input().split(' '))

if (m <= 2):
    print("NEWBIE!")
elif ((m > 2) and (m <= n)):
    print("OLDBIE!")
else:
    print("TLE!")