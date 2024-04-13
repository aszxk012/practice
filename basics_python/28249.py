# 28249
# 고추를 추가할 때마다 매운 정도 출력

peppers = {"Poblano": 1500, "Mirasol": 6000, "Serrano": 15500,
           "Cayenne": 40000, "Thai": 75000, "Habanero": 125000}
total = 0

n = int(input())

for i in range(n):
    pepper = input()
    total += peppers[pepper]

print(total)