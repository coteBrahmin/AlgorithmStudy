#31256KB, 40ms
#일단 인풋값 N을 받아옵니다. 
#num을  전체 줄 수 2*N-1로 할당하였습니다. 

import sys

N = int(sys.stdin.readline())
num = 2*N -1

#그리고 N줄까지의 경우, 뒤의 N-1줄의 경우를 나누어 for문을 통해 별찌기를 반복합니다.
#N줄까지의 경우, num - (2*i-1)을 2로 나눈 몫만큼 공백을, (2*i -1)만큼 별을 출력
#그 이후부터는, 공백을 N 번 + 별을 (num - j*2)번 찍어줍니다. 

for i in range(1, N+1):
    print(" "* ((num-(i*2-1))//2)+ "*"*(i*2-1))
for j in range(1, N):
    print(" "*j + "*" * (num - j*2))