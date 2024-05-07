# 12100
# 삼성 SW 역량 테스트 기출 문제
# 첫째 줄에 보드의 크기 N이 주어지고, 둘째 줄부터 N개의 줄까지 게임판의 초기 상태가 주어진다.
# 0은 빈 칸을 나타내며 블록에 쓰여있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다.
# 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.
# 풀기 시작: 2024.05.05.

n = int(input())
board = []
max_num = 0

# board에 숫자 넣기
for _ in range(n):
    nums = list(map(int, input().split(' ')))
    nums_max = max(nums)
    if (max_num < nums_max):
        max_num = nums_max
    board.append(nums)

# 이동하려고 하는 쪽의 칸 먼저 합쳐짐
# 2 \n 2 \n 2 상태에서 ↑ 누르면 4 \n 2

def transfer(board):
    pass
