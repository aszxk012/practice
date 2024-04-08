# 6763
# 제한속도와 현재 속도가 주어질 때 제한속도보다 1 ~ 20km/h 빠르면 $100
# 제한속도보다 21 ~ 30km/h 빠르면 $270
# 제한속도보다 31km/h 이상 빠르면 $500
# 속도 위반을 하지 않는다면 "Congratulations, you are within the speed limit!",
# 속도 위반을 했다면 "You are speeding and your fine is $F."
# F는 표에 제시된 벌금의 양

standard = int(input())
current = int(input())
diff = current - standard

if (diff <= 0):
    print("Congratulations, you are within the speed limit!")

elif (1 <= diff <= 20):
    print("You are speeding and your fine is $100.")

elif (21 <= diff <= 30):
    print("You are speeding and your fine is $270.")

else:
    print("You are speeding and your fine is $500.")