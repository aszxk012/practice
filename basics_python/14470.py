# 14470
# A도의 고기를 전자레인지로 B도까지 데우려고 한다.
# 고기 온도는 0도보다 낮으면 얼어있고, 높으면 얼어있지 않고, 같다면 얼어 있을 수도, 얼어있지 않을수도 있다.
# 고기가 얼어있고 온도가 0도 미만일때: 온도가 C초에 1도씩 오른다.
# 고기가 얼어있고 온도가 0도일때: 해동하는데 D초가 걸린다.
# 고기가 얼어있지 않을 때: 온도가 E초에 1도씩 오른다.
# B도까지 데워지는데 몇 초가 걸리는지 출력

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

sum = 0

if (a < 0):
    diff = (0 - a) * c
    sum = diff + d

    diff = b * e
    sum += diff

else:
    sum += (b - a) * e

print(sum)