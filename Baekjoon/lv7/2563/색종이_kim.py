#메모리 31256kb, 시간 44ms
import sys
N = int(sys.stdin.readline())
#100 * 100 짜리의 0으로 된 도화지 행렬(board)을 만들어서, 
#해당 되는 색종이의 부분만큼 값을 1로 바꾸어 1의 개수를 카운트 할 것이다
board = [[0 for i in range(100)] for j in range(100)]
count = 0
for _ in range(N):
    x,y = map(int,sys.stdin.readline().split())
    #인덱스가 있기 때문에 y-1부터 y+9까지의 10칸 
    for k in range(y-1,y+9):
        for l in range(x-1,x+9):
            #이미 1인 것이라도 덮어씌우면 1이기 때문에 굳이 조건문 달지 않았음
            board[k][l] = 1 
#전체 행렬의 y축을 돌면서 1을 카운트 
for m in range(100):
    count += board[m].count(1)
print(count)