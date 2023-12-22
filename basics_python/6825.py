# 6825
# BMI 공식은 체중 / (신장 * 신장)(kg/m^2)이다.
# 체중과 신장이 주어질때 BMI가 25 초과면 "Overweight"
# 18.5 이상 25 이하면 "Normal weight", 18.5 미만이면 "Underweight" 출력하기

weight = float(input())
height = float(input())
bmi = weight / (height * height)

if (bmi > 25):
    print("Overweight")
elif ((bmi >= 18.5) and (bmi <= 25)):
    print("Normal weight")
else:
    print("Underweight")