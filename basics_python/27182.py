# 27182
# 오늘은 일요일이고 날짜는 n일이다.
# 저저번주 일요일의 날짜는 m일일때, 저번주 일요일의 날짜 출력
# 한달은 28, 29, 30, 31일 중 하나이다.

n, m = map(int, input().split(' '))
last = n - 7

if (last < 1):
    last = m + 7

print(last)