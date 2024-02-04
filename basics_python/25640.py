# 25640
# 진호의 MBTI 유형이 주어지고 진호의 친구 수와 각 친구들의 MBTI 유형이 주어진다.
# 진호와 MBTI 유형이 같은 사람의 수 출력

mbti = input().upper()
n = int(input())
count = 0

for _ in range(n):
    fr_mbti = input().upper()

    if (fr_mbti == mbti):
        count += 1

print(count)