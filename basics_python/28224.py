# 28224
# 첫 번째 줄에 관측한 기간을 나타내는 정수(일)가 주어진다.
# 두 번째 줄에 첫 번째 날의 원하는 상품의 초기 가격이 주어지고
# 그 다음 줄에는 2일부터 n일까지의 순서대로 해당 상품의 일일 가격 변동을 나타내는 정수가 주어진다.
# 상품의 최종 가격 출력

n = int(input())
initial = int(input())
final = initial

for i in range(1, n):
    cur_pri = int(input())
    final += cur_pri

print(final)