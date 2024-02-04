# 21591
# 노트북과 함께 제공된 스티커를 각 변에 1cm 공간을 남기고 붙이려고 할 때
# 붙일 수 있는지(1) 없는지(0) 출력, 회전 불가능
# wc, hc는 노트북의 너비, 높이이고 ws, hs는 스티커의 너비, 높이이다.

wc, hc, ws, hs = map(int, input().split(' '))
wc -= 1
hc -= 1

if ((ws < wc) and (hs < hc)):
    print(1)
else:
    print(0)