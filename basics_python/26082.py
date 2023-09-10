# 26082
# 성능이 경쟁사 제품의 3배, 가격 대비 성능 = 성능 / 가격
# 경쟁사 제품의 가격, 경쟁사 제품의 성능, warboy의 가겨이 주어질떄
# warboy의 성능 구하기

a, b, c = map(int, input().split(' '))

enem = b // a
my = enem * 3


print(my * c)