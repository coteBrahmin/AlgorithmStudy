#메모리 31256kb, 시간 48ms
import sys
N,M = map(int,sys.stdin.readline().split())
#일단 줄 단위로 묶은 2차원 리스트를 만든다
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N*2)]
#앞에서부터 N줄씩 행렬을 만든다 
A = matrix[:N]
B = matrix[N:]
ans = []
#N줄은 세로로 진행
for i in range(N):
    #연산한 값을 넣어줄 가로줄 리스트 
    row = []
    #M줄은 가로로 진행
    for j in range(M):
        row.append(A[i][j]+B[i][j])    
    ans.append(row)
for k in range(N):
    print(*ans[k])