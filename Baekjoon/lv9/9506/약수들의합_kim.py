#memory 31120kb, time 64ms
import sys
while True:
    N = int(sys.stdin.readline())
    if N == -1:
        break
    else:
        yaksoo = 0
        printyaksoo = ''
        for i in range(1,N):
            if N % i == 0:
                yaksoo += i
                printyaksoo += f'{i} + '
        if yaksoo == N: print(f'{yaksoo} = {printyaksoo[:-2]}')
        else: print(f'{N} is NOT perfect.')