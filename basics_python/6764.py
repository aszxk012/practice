# 6764
# 네 번의 연속된 깊이 탐지 결과가 증가 수열을 이루거나(Fish Rising)
# 네 번의 연속된 깊이 탐지 결과가 감소 수열을 이루거나(Fish Diving)
# 네 번의 연속된 깊이 탐지가 동일한 경우(Fish At Constant Depth)거나
# 모든 결과에 해당하지 않는 경우(No Fish)
# 각 경우에 해당할 경우 깊이 탐지 결과를 출력한다

a = int(input())
b = int(input())
c = int(input())
d = int(input())


if ((a < b) and (b < c) and (c < d)):
    print("Fish Rising")
elif ((a > b) and (b > c) and (c > d)):
    print("Fish Diving")
elif ((a == b) and (b == c) and (c == d)):
    print("Fish At Constant Depth")
else:
    print("No Fish")