#메모리 31256kb, 시간 40ms
import sys
#입력을 가로줄 단위로 받을 때 그 줄에서 제일 큰 값을 모은 리스트
#이 리스트의 인덱스는 1~9까지의 세로줄을 의미하고 최종 값의 좌표가 (c,r)라고 할때 c값이 된다
row_max = []
#각 가로줄마다 있는 최대값의 그 줄에서의 인덱스는 최종 값의 좌표가 (c,r)라고 할때 r값이 된다
row_max_index = []
for _ in range(9):
    row = list(map(int,sys.stdin.readline().split()))
    row_max.append(max(row))
    row_max_index.append(row.index(max(row)))
#각 행들의 최대값들 중에서 가장 큰 최종 최대값
maxiest = max(row_max)
print(maxiest)
print(row_max.index(maxiest)+1,row_max_index[row_max.index(maxiest)]+1)