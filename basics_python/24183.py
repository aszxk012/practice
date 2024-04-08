# 24183
# 우편은 세 가지로 이루어져 있고, 각각의 크기는 다음과 같다.
# C4 크기의 봉투(229mm * 324mm)
# A3 크기의 포스터 2개 (297mm * 420mm)
# A4 크리의 대회 안내지 (210mm * 297mm)
# 우편은 50g을 초과해서는 안되며 종이 무게의 기본 단위는 g / m^2이다.
# C4 크기의 봉투는 C4 크기의 종이 두 장을 붙여 만들었다.
# 우편의 총 무게 출력
# 정답은 소수점 셋째자리까지 일치해야함

c4, a3, a4 = map(int, input().split(' '))
c4_area = 0.229 * 0.324
a3_area = 0.297 * 0.42
a4_area = 0.21 * 0.297

c4_w = c4_area * c4 * 2
a3_w = a3_area * a3 * 2
a4_w = a4_area * a4

total = c4_w + a3_w + a4_w

print(total)