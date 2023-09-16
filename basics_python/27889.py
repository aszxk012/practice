# 27889
# 학교 이름 약칭이 주어졌을 때 정식 명칭 출력하기

school = {"NLCS": "North London Collegiate School",
          "BHA": "Branksome Hall Asia",
           "KIS": "Korea International School",
           "SJA": "St. Johnsbury Academy"}

string = input()

for key in school:
    if key == string:
       print(school[key])
    