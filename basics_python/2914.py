# 2914
# 저작권이 있는 멜로디의 평균값 구하기
# 저작권이 있는 멜로디의 개수 / 앨범에 수록된 곡의 개수 > 반올림 되있을 수도 있음
# 앨범에 수록된 곡의 개수와 평균값이 주어졌을 때 적어도 몇 곡이 저작권 있는 멜로디인지 출력하기

char = input()
melody, rights = char.split(' ')
melody, rights = int(melody), int(rights)

rights -= 1

print(melody * rights + 1)