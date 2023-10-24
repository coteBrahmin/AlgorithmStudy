#메모리 31120kb, 시간 40ms
import sys
while True:
    A,B = map(int,sys.stdin.readline().split())
    if A == 0 and B == 0:
        break
    else:
        if B % A == 0:
            print("factor")
        elif A % B == 0:
            print("multiple")
        else :
            print("neither")