# 22015
# A, B, C가 각각 a, b, c개의 사탕을 먹었다.
# 세 사람이 먹은 사탕의 개수를 똑같이 하기 위해 최소 몇 개의 사탕을 추가로 먹어야하는지 출력하기

candies = list(map(int, input().split(' ')))
max_candy = max(candies)
result = 0

if (max_candy == candies[0]):
    temp_a = max_candy - candies[1]
    temp_b = max_candy - candies[2]
    result = temp_a + temp_b

elif (max_candy == candies[1]):
    temp_a = max_candy - candies[0]
    temp_b = max_candy - candies[2]
    result = temp_a + temp_b

elif (max_candy == candies[2]):
    temp_a = max_candy - candies[0]
    temp_b = max_candy - candies[1]
    result = temp_a + temp_b

print(result)