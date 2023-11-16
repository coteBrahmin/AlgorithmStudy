# 메모리: 31256 KB, 시간: 40 ms 
import sys

matrix= [list(map(int, sys.stdin.readline().split())) for i in range(9)]

max_value = 0
row = 0
col = 0
for i in range(9):
    for j in range(9):
        #최댓값을 max_value에 담아준다.
        #그리고 해당 row, column을 i+1, j+1로 받아온다. 0부터 시작하기 때문에 1을 더해준다.
        if matrix[i][j] > max_value:
            max_value =  matrix[i][j]
            row,col = i+1,j+1
        #최댓값이 여러개일 경우, 마지막에 있는 행과 열의 자리(최신)를 가져오게 설정하였다.
        elif matrix[i][j] == max_value:
            row,col = i+1, j+1

print(max_value)
print(row, col)