# 메모리: 31256 KB, 시간: 56 ms
import sys
N,M = map(int, sys.stdin.readline().split())

#N행 만큼 리스트를 받아와서 2차원 리스트 배열 2개를 만든다.
#예시) matrix1 = [[1, 1, 1], [2, 2, 2], [0, 1, 0]]
matrix1= [list(map(int, sys.stdin.readline().split())) for i in range(N)] 
matrix2= [list(map(int, sys.stdin.readline().split())) for i in range(N)]

#두 행렬의 같은 위치의 원소 matrix[i][j]를 더해준다.
#행마다 개행이 필요하니 N번 개행을 해준다.
for i in range(N):
    for j in range(M):
        print(matrix1[i][j] + matrix2[i][j], end =" ")
    print()
