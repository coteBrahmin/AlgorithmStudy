#memory 31120kb, time 656ms
import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
numlist = list(range(M,N+1))

#for num in numlist로 하면 range가 계속 바뀌어서 그냥 numlist와 별개로 탐색
for num in range(M,N+1):
    if num == 1:
        numlist.remove(1)
        continue
    for i in range(2,num):
        #소수가 아니라면 numlist에서 삭제
        if num % i == 0:
            numlist.remove(num)
            break
if len(numlist) == 0: print(-1)
else:
    print(sum(numlist))
    print(numlist[0])