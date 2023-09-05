# 18409
# 길이 N인 문자열 s가 주어질 때, s의 모음 개수 합 출력하기

n = int(input())
s = input().lower()
vowels = ['a', 'e', 'i', 'o', 'u']
sum = 0

for i in range(n):
    if s[i] in vowels:
        sum += 1
        
print(sum)