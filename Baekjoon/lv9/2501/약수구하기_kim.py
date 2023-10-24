#메모리 31120kb, 시간 44ms
import sys
N,K = map(int,sys.stdin.readline().split())
yaksoo = []
for i in range(1,N+1):
    if N % i == 0: yaksoo.append(i)
if len(yaksoo) < K:
    print(0)
else:
    #인덱스는 0부터 시작하니까 k-1
    print(yaksoo[K-1])