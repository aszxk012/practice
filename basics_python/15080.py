# 15080
# 첫 번째 줄에는 시작 시각이, 두 번째 줄에는 종료 시각이 주어질 때
# 두 시각 사이가 몇 초인지 출력
# 두 시각 차이는 24시간과 같거나 길지 않으며 종료 시각이 시작 시각보다 낮은 값일 수 있음

start = list(map(int, input().split(' : ')))
end = list(map(int, input().split(' : ')))
diff = []
total = 0

for i in range(len(start)):
    diff_tiem = end[i] - start[i]
    diff.append(diff_tiem)

total += diff[0] * 60 * 60
total += diff[1] * 60
total += diff[2]

if (total < 0):
    total += 24 * 60 * 60

print(total)