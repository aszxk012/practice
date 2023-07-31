# 2566
# 9 x 9 행렬에서 최대 값 찾아서 몇 행 몇 열에 위치한 수인지 출력하기

import sys

max_num = -sys.maxsize - 1
row = 0
col = 0
matrix = []

for _ in range(9):
    matrix.append(input().split(' '))
    
for i in range(9):
    for j in range(9):
        matrix[i][j] = int(matrix[i][j])
        
        if max_num < matrix[i][j]:
            max_num = matrix[i][j]
            
print(max_num)

for i in range(9):
    for j in range(9):
        if max_num == matrix[i][j]:
            row = i + 1
            col = j + 1
print(row, col)