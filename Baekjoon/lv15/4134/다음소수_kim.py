import sys

#소수인지 판별하는 함수
def yaksoo(x) :
    isSosoo = 1
    for j in range(1, int(x ** (1 / 2) + 1)):
        if x % j == 0:
            if j == 1:
                continue
            else:
                isSosoo = 0
                break
    return isSosoo

T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    if N != 0 and N != 1:
        #수의 최대 범위가 4*(10**9)인데 N이 최대 범위에 가까운 경우 그것보다 큰 소수까지 탐색이 가능해야함. 
        for k in range(N,4*(10**9)+100):
            if yaksoo(k) :
                print(k)
                break
    else:
        print(2)